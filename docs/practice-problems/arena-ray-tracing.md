---
title: ARENA - 0.1 Ray Tracing
description: |
  My notes and explanation about the exercises for Ray Tracing Exercises in the ARENA curriculum
tags:
  - pytorch
  - numpy
  - linear-algebra
updated_date: 2026-07-02
url: https://learn.arena.education/chapter0_fundamentals/01_ray_tracing/intro/
---

#[ARENA - 0.1 Ray Tracing](https://learn.arena.education/chapter0_fundamentals/01_ray_tracing/intro/)

## Rays and Segments

### Generating rays starting at the origin

We need to implement the function to generate rays coming out of the origin `(0,0,0)`.

We consider each ray to be a line with one end at the origin and the other end at some point in the Y-axis for `x=1`. For now, we leave out the third z-coordinate.

```python
def make_rays_1d(num_pixels: int, y_limit: float) -> Tensor:
    """
    num_pixels: The number of pixels in the y dimension. Since there is one ray per pixel, this is
        also the number of rays.
    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both endpoints.

    Returns: shape (num_pixels, num_points=2, num_dim=3) where the num_points dimension contains
        (origin, direction) and the num_dim dimension contains xyz.

    Example of make_rays_1d(9, 1.0): [
        [[0, 0, 0], [1, -1.0, 0]],
        [[0, 0, 0], [1, -0.75, 0]],
        [[0, 0, 0], [1, -0.5, 0]],
        ...
        [[0, 0, 0], [1, 0.75, 0]],
        [[0, 0, 0], [1, 1, 0]],
    ]
    """
    result = t.zeros(num_pixels, 2, 3) # Number of rays = number of pixels, each ray is identified by 2 points and each point has 3 dimensions
    y_values = t.linspace(-y_limit, y_limit, num_pixels) # Create evenly spaced y values from -y_limit to y_limit
    result[:, 1, 0] = 1.0 # Set the x-coordinate of the direction point to 1.0 for all rays
    result[:, 1, 1] = y_values # Set the y-coordinate of the direction point to the computed y values
    return result
```

### How do we find whether a camera ray and an object line intersect?

We can represent every point on the ray and the line segment using parametric equations

$$
\begin{aligned}
\text{Ray: } & R(u) = O + uD \\
\text{Object Line: } & O(v) = L_1 + v(L_2 - L_1)
\end{aligned}
$$

Here:

- $u$ and $v$ are the scalar parameters for the ray and object line respectively.
- $O$ is the camera origin (where the ray starts).$D$ is the direction vector the ray is shooting toward.
- $u$ is the "time" or distance traveled along the ray. Because a ray starts at the camera and shoots forward infinitely, $u$ must be greater than or equal to $0$ ($u \in [0, \infty)$).
- $L_1$ and $L_2$ are the endpoints of the segment.
- $(L_2 - L_1)$ is the vector pointing from $L_1$ to $L_2$.
- $v$ is the interpolation factor. If $v = 0$, you are exactly at $L_1$. If $v = 1$, you are at $L_2$. Therefore, to stay inside the actual segment, $v$ must be between $0$ and $1$ ($v \in [0, 1]$).

Geometrically, two infinite lines in a 2D plane will always intersect at exactly one point, unless they are perfectly parallel.To find this point, we set the two equations equal to each other:

$$
O + uD = L_1 + v(L_2 - L_1)
$$

Because we are working in 2D space, this single vector equation breaks down into a system of two linear equations (one for the $X$-axis, one for the $Y$-axis):

- $O_x + uD_x = L_{1x} + v(L_{2x} - L_{1x})$
- $O_y + uD_y = L_{1y} + v(L_{2y} - L_{1y})$

Using algebra (like Cramer's Rule or substitution), you solve for the two unknowns: $u$ and $v$.

Just because the infinite lines intersect doesn't mean your actual ray hits the actual segment. The values of $u$ and $v$ tell you exactly where the intersection happened relative to your boundaries:

- If $u < 0$ the intersection happens behind the camera -> (Miss). A negative time ($u = -2$) means you are looking backward, behind the camera. Mathematically, the infinite lines intersect, but physically, the object is behind your head, so the camera ray misses it.
- If $u \ge 0$, the intersection happens in front of the camera -> (Hit). When $u = 0$, you are standing exactly at the camera origin ($O$). As $u$ increases ($1, 2, 10.5\dots$), you are moving forward in the direction the camera is looking. An intersection here means the camera can actually "see" the object.
- If $v < 0$ or $v > 1$, the intersection happens on the infinite line, but outside the $L_1 \rightarrow L_2$ segment. -> (Miss). If $v = -0.5$, you went backward past the starting point $L_1$.If $v = 1.5$, you shot past the endpoint $L_2$.While the ray hit the infinite trajectory of the line, it missed the actual, finite stick.
- If $0 \le v \le 1$The intersection happens directly on the line segment. -> (Hit). At $v = 0$, the equation becomes $L_1 + 0$, which is exactly the start of the segment ($L_1$).At $v = 0.5$, you are exactly halfway between $L_1$ and $L_2$.At $v = 1$, the equation simplifies to $L_1 + (L_2 - L_1) = L_2$, which is exactly the end of the segment.Therefore, any value between $0$ and $1$ means the intersection point lies physically on the fabric of the segment.

For a valid hit, both conditions must be true simultaneously:$$u \ge 0 \quad \text{AND} \quad 0 \le v \le 1$$If the solved $u$ and $v$ satisfy those boundaries, you plug $u$ back into $R(u)$ (or $v$ into $O(v)$) to get the exact $(x, y)$ coordinate where the ray punctures the object.

```python
def intersect_ray_1d(ray: Float[Tensor, "points dims"], segment: Float[Tensor, "points dims"]) -> bool:
    """
    ray: shape (n_points=2, n_dim=3)  # O, D points
    segment: shape (n_points=2, n_dim=3)  # L_1, L_2 points

    Return True if the ray intersects the segment.
    """

    """
    Equation is O + uD = L_1 + v (L_2 - L_1).
    The equation can be used for both x and y coordinates.
    O_x + uD_x = L_1_x + v (L_2_x - L_1_x) and O_y + uD_y = L_1_y + v (L_2_y - L_1_y)
    The 2 equations can be stacked together to form a linear system Ax = b, where:
        x = [u, v]^T
        A is [[D_x, -(L_2_x - L_1_x)], [D_y, -(L_2_y - L_1_y)]]
        b = [L_1_x - O_x, L_1_y - O_y]^T
    """

    # Defining A, x, b
    O, D = ray[0, :2], ray[1, :2]  # Extracting the origin and direction points from the ray
    L_1, L_2 = segment[0, :2], segment[1, :2] # Extracting the endpoints of the segment
    A = t.tensor([[D[0], -(L_2[0] - L_1[0])], [D[1], -(L_2[1] - L_1[1])]])
    b = t.tensor([L_1[0] - O[0], L_1[1] - O[1]])
    try:
        x = t.linalg.solve(A, b)
        if t.isnan(x).any():
            return False
        else:
            if (x[0] >= 0) and (0 <= x[1] <= 1):
                return True
            else:
                return False
    except RuntimeError:
        return False
```

## Batched Operations

### Batched Ray-Segment Intersection

The [previous section](#rays-and-segments) walks through how to check if a ray from a camera and an object line intersect at valid points. But we can have multiple camera rays and multiple object lines, all of which can form their own pairs of possible intersections.

To find if there are valid intersections between multiple camera rays and object line segments, we can expand the matrix calculation with new dimensions.

```python
def intersect_rays_1d(
    rays: Float[Tensor, "nrays 2 3"], segments: Float[Tensor, "nsegments 2 3"]
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if it intersects any segment.
    """
    # Using einops to repeat rays and segments to create a grid of all possible intersection combinations
    rays_expanded = einops.repeat(rays, "nr p c -> nr ns p c", ns = segments.shape[0])
    segments_expanded = einops.repeat(segments, "ns p c -> nr ns p c", nr = rays.shape[0])

    # Getting the origin and direction points from the rays and the endpoints from the segments
    O = rays_expanded[:, :, 0, :2]  # shape (nrays, nsegments, 2)
    D = rays_expanded[:, :, 1, :2]  # shape (nrays, nsegments, 2)
    L_1 = segments_expanded[:, :, 0, :2]  # shape (nrays, nsegments, 2)
    L_2 = segments_expanded[:, :, 1, :2]  # shape (nrays, nsegments, 2)

    # Construct matrix for each ray and segment pair
    A = t.stack([D, -(L_2 - L_1)], dim=-1)  # shape (nrays, nsegments, 2, 2)

    # Construct the RHS vector for the linear system of equations
    b = L_1 - O  # shape (nrays, nsegments, 2)

    # Find determinants for each ray-segment pair to check for singularity
    det_A = t.linalg.det(A)  # shape (nrays, nsegments)
    is_singular = det_A.abs() < 1e-8  # shape (nrays, nsegments)

    # Unsqueeze is_singular from (nr, ns) -> (nr, ns, 1, 1) to broadcast with (nr, ns, 2, 2)
    # t.eye(2) will automatically broadcast its trailing (2, 2) dimensions
    A_safe = t.where(is_singular.unsqueeze(-1).unsqueeze(-1), t.eye(2), A)

    # Solve the linear system
    # Note: matrix (nr, ns, 2, 2) and vector b (nr, ns, 2) matches natively, no squeeze needed!
    x = t.linalg.solve(A_safe, b)
    u, v = x[..., 0], x[..., 1]  # shape (nrays, nsegments)

    # Apply logic conditions to determine if rays intersect segments in front of the camera and within the segment bounds
    intersects = (u >= 0) & (v >= 0) & (v <= 1) & (~is_singular)  # shape (nrays, nsegments)

    return intersects.any(dim=1)  # shape (nrays,)
```

**Grid Expansion**

```python
rays_expanded = einops.repeat(rays, "nr p c -> nr ns p c", ns = segments.shape[0])
segments_expanded = einops.repeat(segments, "ns p c -> nr ns p c", nr = rays.shape[0])
```

We are given `nr` number of rays, each ray represented by the pair `O, D` where `O` is the origin, `D` is the direction of the ray from the origin. Similarly, we have `ns` number of line segments, each segment is represented by the start and end points `L1, L2` respectively. Note that each point in the ray and segment line is of 3 dimensions `(x,y,z)`, although for the purpose of this question we consider only x and y coordinates.

To get all possible pairs of rays and line segments, we need all possibles pairs of `(O,D)` and `(L1, L2)`. We can do this by adding 1 extra dimension to both rays and segments, to accomodate the other part of the pair - add dimension of `ns` to rays and `nr` to segments. This gives a 2D grid combining every single ray with every single segment so they can be processed simultaneously.

Example Mapping:

- `rays_expanded[0, 0]` and `rays_expanded[0, 1]` both contain the data for Ray 0.
- `segments_expanded[0, 0]` contains Segment 0; `segments_expanded[0, 1]` contains Segment 1.

**Slicing out 2D Plane Coordinates**

```python
O = rays_expanded[:, :, 0, :2]  # shape (nrays, nsegments, 2)
D = rays_expanded[:, :, 1, :2]  # shape (nrays, nsegments, 2)
L_1 = segments_expanded[:, :, 0, :2]  # shape (nrays, nsegments, 2)
L_2 = segments_expanded[:, :, 1, :2]  # shape (nrays, nsegments, 2)
```

We get `O,D` from rays and `L1, L2` from the segments for all ray-segment pairs. Slicing with :2 isolates the $(x, y)$ coordinates and removes the unused $z$ coordinate, adapting 3D dataset layouts into a pure 2D coplanar space.

**Setting up the linear system of equations**

```python
A = t.stack([D, -(L_2 - L_1)], dim=-1)  # shape (nrays, nsegments, 2, 2)
b = L_1 - O  # shape (nrays, nsegments, 2)
```

Recall the original equation [here](#how-do-we-find-whether-a-camera-ray-and-an-object-line-intersect). We set up the intersection matrix once again, but this time we define the matrix to hold the intersections of all possible ray-segment pairs.

Each ray-segment pair's equation is stacked one after the other in the last dimension to finally get all the pairs' equations in the single matrix `A`.

**Singularity Check**

```python
det_A = t.linalg.det(A)  # shape (nrays, nsegments)
is_singular = det_A.abs() < 1e-8  # shape (nrays, nsegments)
```

If a ray-segment pair is parallel to each other then their corresponding matrix `A` will be singular, that is, their determinant will be 0. It is not possible to find points of intersection for parallel lines and can cause divsion-by-zero error with linear solvers, hence we need to avoid solving the equations for such pairs.

**Identity Matrix Masking**

```python
A_safe = t.where(is_singular.unsqueeze(-1).unsqueeze(-1), t.eye(2), A)
```

Once the parallel pairs have been identified, their equations can be replaced with the identity matrix. `unsqueeze(-1).unsqueeze(-1)` changes is_singular's shape from \[1, 2\] to \[1, 2, 1, 1\] so it can broadcast over the $2 \times 2$ matrices. Any parallel pair matrix is replaced with a standard identity matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ to act as a placeholder. This keeps the execution pipeline entirely on the GPU without throwing errors.

**Solving the Matrices**

```python
x = t.linalg.solve(A_safe, b)
u, v = x[..., 0], x[..., 1]  # shape (nrays, nsegments)
```

All the linear systems across ray-segment pairs are solved simultaneously to get `u` and `v`

**Intersection Bounds Masking**

```python
intersects = (u >= 0) & (v >= 0) & (v <= 1) & (~is_singular)  # shape (nrays, nsegments)
```

Even if there are possible intersections of ray-segment pairs, they need to valid intersections. Validating the physical rules:

- `u >= 0`: The hit point is in front of the ray's origin, not backwards.
- `v >= 0 & v <= 1`: The hit point lies along the bounded segment length.
- `~is_singular`: A protective filter that discards any "fake" answers produced by the identity matrix placeholder step.

**Batch Reduction**

```python
return intersects.any(dim=1)  # shape (nrays,)
```

`intersects[i,j]` stores boolean results of whether ray `i` and segment `j` intersect at valid points. Thus, we can now find, for every ray, if there is atleast one valid intersecting segment.

### Generating 2D Rays

Till now, we looked at 1D rays identified by the origin `O` and direction `D`, but each point considered only the X and Y coordinates. Now, we move towards defining rays with a Z component as well.

```python
def make_rays_2d(num_pixels_y: int, num_pixels_z: int, y_limit: float, z_limit: float) -> Float[Tensor, "nrays 2 3"]:
    """
    num_pixels_y: The number of pixels in the y dimension
    num_pixels_z: The number of pixels in the z dimension

    y_limit: At x=1, the rays should extend from -y_limit to +y_limit, inclusive of both.
    z_limit: At x=1, the rays should extend from -z_limit to +z_limit, inclusive of both.

    Returns: shape (num_rays=num_pixels_y * num_pixels_z, num_points=2, num_dims=3).
    """

    result = t.zeros(num_pixels_y * num_pixels_z, 2, 3)  # Initialize the result tensor
    y_values = t.linspace(-y_limit, y_limit, num_pixels_y)  # Create evenly spaced y values from -y_limit to y_limit
    z_values = t.linspace(-z_limit, z_limit, num_pixels_z)  # Create evenly spaced z values from -z_limit to z_limit
    y_grid, z_grid = t.meshgrid(y_values, z_values, indexing='ij')  # Create a grid of y and z values
    result[:, 1, 0] = 1.0  # Set the x-coordinate of the direction point to 1.0 for all rays
    result[:, 1, 1] = y_grid.flatten()  # Set the y-coordinate of the direction point to the flattened y grid
    result[:, 1, 2] = z_grid.flatten()  # Set the z-coordinate of the direction point to the flattened z grid
    return result
```

**Defining result tensor**

What should the shape of the final result tensor be? We can estimate the last 2 dimensions as 2 (number of points defining the ray) and 3 (number of dimensions per point).

What about the number of rays? Each ray is defined by one pixel, and the total number of available pixels is `num_pixels_y * num_pixels_z`, which is also the first dimension of the result tensor

**Defining range of Y and Z pixel values**

```python
y_values = t.linspace(-y_limit, y_limit, num_pixels_y)
z_values = t.linspace(-z_limit, z_limit, num_pixels_z)
y_grid, z_grid = t.meshgrid(y_values, z_values, indexing='ij')
```

We can generate possible Y and Z axis pixel values using `linspace` as 1D arrays of evenly spaced coordinates. Once we have the initial coordinates, we can define a mesh of Y-Z pixel coordinates, and the `indexing='ij'` ensures that rows correspond to Y coordinates and columns to Z coordinates

**Defining result destination coordinates**

```python
result[:, 1, 0] = 1.0
result[:, 1, 1] = y_grid.flatten()
result[:, 1, 2] = z_grid.flatten()
```

Every result ray consists of 2 points. The first is already defined during initialization - the origin. For the destination point, we know all X coordinates are equal to 1.
Finally we then set the Y and Z coordinates by flattening the Y and Z coordinate grids to get 1D sequences of numbers

## Triangles

### Implement `triangle_ray_intersects`

The objective here is to find if there is a valid intersection point between a triangle and a ray. In the [previous section](#batched-operations), we looked at the intersection of multiple rays with a plane. Now we restrict the plane to a triangle and check for the same validations.

We use a variation of the Möller–Trumbore intersection algorithm to determine if a 3D ray intersects the 3 D triangle.

Let the 3 vertices of the triangle be &A, B, C$. To identify a point within the triangle, we can use the concept of barycentric coordinates such that

$$
\begin{aligned}
& P(w, u, v) = wA + uB + vC \\
& \text{s.t.} \quad w + u + v = 1 \\
& \quad \quad w, u, v \ge 0
\end{aligned}
$$

We can reduce this further by substituting $w = 1 - u - v$ to get the equation

$$
\begin{aligned}
P(u, v) &= (1 - u - v)A + uB + vC \\
&= A + u(B - A) + v(C - A) \\
\text{s.t.} \quad & u, v \ge 0 \\
& u + v \le 1
\end{aligned}
$$

Here, $u,v$ are called barycentric coordinates. The constraints on $u, v$ ensure that the points obtained from the equation always lie in the triangle, and not anywhere on the plane in which the triangle exists.

For a camera ray and the triangle to intersect, we need

$$
\begin{aligned}
P(u,v) = P(s) \implies & A + u(B - A) + v(C - A) = O + sD \\
\implies & \begin{pmatrix} -D & B - A & C - A \end{pmatrix} \begin{pmatrix} s \\ u \\ v \end{pmatrix} = O - A \\
\implies & \begin{pmatrix}
-D_x & (B - A)_x & (C - A)_x \\
-D_y & (B - A)_y & (C - A)_y \\
-D_z & (B - A)_z & (C - A)_z
\end{pmatrix}
\begin{pmatrix} s \\ u \\ v \end{pmatrix} =
\begin{pmatrix} (O - A)_x \\ (O - A)_y \\ (O - A)_z \end{pmatrix}
\end{aligned}
$$

**Defining the $ 3 \times 3$ matrix `M` for the equation LHS, and `b` the equation RHS**

```python
M = t.stack([-D, B-A, C-A], dim=1)  # shape (3, 3)
b = O - A  # shape (3,)
```

**Linear Solver to solve the equation system**

```python
x = t.linalg.solve(M, b)  # shape (3,)
s, u, v = x
if s >= 0 and u >= 0 and v >= 0 and (u + v) <= 1:
    return True
else:
    return False
```

### Implement `raytrace_triangle`

We expand further from the previous section where multiple rays have the possibility of intersecting with the triangle. Since the linear solver in pytorch handles simulatenous solving of systemn of equations, we can reutilize much of the logic from the `triangle_ray_intersects` function and augment it by expanding the dimensions to accomodate multiple rays

```python
def raytrace_triangle(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangle: Float[Tensor, "trianglePoints=3 dims=3"],
) -> Bool[Tensor, " nrays"]:
    """
    For each ray, return True if the triangle intersects that ray.
    """

    """
    The system of equations needs to be expanded to accomodate nrays instead of 1 ray.
    This means adding an extra dimension to the traingle points to repeat it across nrays
    """
    triangle_expanded = einops.repeat(triangle, "points dims -> nrays points dims", nrays = rays.shape[0])
    O, D = rays[:, 0, :], rays[:, 1, :]  # shape (nrays, 3)
    A, B, C = triangle_expanded[:, 0, :], triangle_expanded[:, 1, :], triangle_expanded[:, 2, :]  # shape (nrays, 3)
    M = t.stack([-D, B-A, C-A], dim=-1)  # shape (nrays, 3, 3)
    b = O - A  # shape (nrays, 3)
    try:
        s,u,v = t.linalg.solve(M, b).T
        intersects = (s >= 0) & (u >= 0) & (v >= 0) & ((u + v) <= 1)
        return intersects
    except t.linalg.LinAlgError:
        return t.zeros(rays.shape[0], dtype=t.bool)
```

### Implement `raytrace_mesh`

If we go to the next step, we can have simultaneous intersections between multiple rays and multiple triangles. This leads to expansion of dimensions to accomodate both rays and triangles.

```python
def raytrace_mesh(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.
    """
    """
    The system of equations needs to be expanded to accomodate nrays and ntriangles instead of 1 ray and 1 triangle.
    This means adding an extra dimension to the traingle points to repeat it across nrays
    """
    triangles_expanded = einops.repeat(triangles, "ntriangles trianglePoints dims -> nrays ntriangles trianglePoints dims", nrays = rays.shape[0])
    assert triangles_expanded.shape == (rays.shape[0], triangles.shape[0], 3, 3)

    rays_expanded = einops.repeat(rays, "nrays rayPoints dims -> nrays ntriangles rayPoints dims", ntriangles = triangles.shape[0])
    assert rays_expanded.shape == (rays.shape[0], triangles.shape[0], 2, 3)

    O, D = rays_expanded[:, :, 0, :], rays_expanded[:, :, 1, :]  # shape (nrays, ntriangles, 3)
    assert O.shape == (rays.shape[0], triangles.shape[0], 3)
    assert D.shape == (rays.shape[0], triangles.shape[0], 3)

    A, B, C = triangles_expanded[:, :, 0, :], triangles_expanded[:, :, 1, :], triangles_expanded[:, :, 2, :]  # shape (nrays, ntriangles, 3)
    assert A.shape == (rays.shape[0], triangles.shape[0], 3)
    assert B.shape == (rays.shape[0], triangles.shape[0], 3)
    assert C.shape == (rays.shape[0], triangles.shape[0], 3)

    M = t.stack([-D, B-A, C-A], dim=-1)  # shape (nrays, ntriangles, 3, 3)
    assert M.shape == (rays.shape[0], triangles.shape[0], 3, 3)

    b = O - A  # shape (nrays, ntriangles, 3)
    assert b.shape == (rays.shape[0], triangles.shape[0], 3)

    # Handle singular matrices without crashing the entire batch
    dets = t.linalg.det(M)                      # (nrays, ntriangles)
    is_singular = t.abs(dets) <= 1e-8          # (nrays, ntriangles)
    M[is_singular] = t.eye(3)  # Replace singular matrices with identity

    try:
        x = t.linalg.solve(M, b)  # shape (nrays, ntriangles, 3)
        s,u,v = x[..., 0], x[..., 1], x[..., 2]
        s *= D[..., 0]
        intersects = (u >= 0) & (v >= 0) & ((u + v) <= 1) & (~is_singular)
        s[~intersects] = float("inf")
        return einops.reduce(s, "NR NT -> NR", "min")
    except t.linalg.LinAlgError:
        return t.full((rays.shape[0],), float("inf"))
```

An addition piece of logic is to first determine if any pair of ray-triangle does not have any intersections. The linear solver can throw errors in such cases, hence we can use the determinant to find such pairs and set their corresponding LHS matrices to the identity matrix of shape $3 \times 3$.

## Exercise - rotation matrix

The objective is to create a matrix which can introduce a counterclockwise transformation of angle $\theta$ around the y-axis. Mathematically, the following $3 \times 3$ matrix can introduce the rotation when given coordinates across X, Y, and Z axes

$$
$$R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}$$
$$

```python
def rotation_matrix(theta: Float[Tensor, ""]) -> Float[Tensor, "rows cols"]:
    """
    Creates a rotation matrix representing a counterclockwise rotation of `theta` around the y-axis.
    """
    rot_mat = t.tensor([[t.cos(theta), 0, t.sin(theta)],
                        [0, 1, 0],
                        [-t.sin(theta), 0, t.cos(theta)]])
    return rot_mat
```

## Exercise - use GPUs

Recall the `raytrace_mesh` function in the [previous section](#implement-raytrace_mesh). Till now, we have done all the computations using the CPU. As the computations grow in volume and complexity, using dedicated GPUs speeds up the process.

```python
def raytrace_mesh_gpu(
    rays: Float[Tensor, "nrays rayPoints=2 dims=3"],
    triangles: Float[Tensor, "ntriangles trianglePoints=3 dims=3"],
) -> Float[Tensor, " nrays"]:
    """
    For each ray, return the distance to the closest intersecting triangle, or infinity.

    All computations should be performed on the GPU.
    """
    device = t.device("cuda" if t.cuda.is_available() else "cpu")
    rays = rays.to(device)
    triangles = triangles.to(device)
    dists = raytrace_mesh(rays, triangles)
    return dists.cpu()
```

## Exercise (bonus) - Add Lighting

We can enhance the rendered 3D figure by varying the light intesnities across the different composite triangles. Mathematically, this brightness is determined by the angle between two vectors:

- The Light Vector ($\vec{L}$): The direction the light is coming from.
- The Normal Vector ($\vec{N}$): An arrow sticking straight out of the surface (like a flagpole sticking out of a roof).

According to Lambert's Cosine Law, the intensity of the reflection depends on the dot product of these two normalized (unit) vectors:

$$
\text{Intensity} = \vec{N} \cdot \vec{L} = \cos(\theta)
$$

**1. Finding out what we actually hit**

```python
closest_distances = raytrace_mesh(rays, triangles)
```

Before doing any math, the code fires thousands of "rays" from the camera into the 3D scene. It calls a helper function raytrace_mesh to find out the distance ($s$) to the closest triangle each ray collides with. If a ray misses everything, it returns an infinite distance (`inf`).

**2. Finding the closest triangle based on the closest distance**

```python
# We rebuild the broadcasted arrays exactly like inside raytrace_mesh
NR = rays.size(0)
NT = triangles.size(0)

triangles_expanded = einops.repeat(triangles, "NT pts dims -> NR NT pts dims", NR=NR)
A, B, C = triangles_expanded[:, :, 0, :], triangles_expanded[:, :, 1, :], triangles_expanded[:, :, 2, :]

rays_expanded = einops.repeat(rays, "NR pts dims -> NR NT pts dims", NT=NT)
O, D = rays_expanded[:, :, 0, :], rays_expanded[:, :, 1, :]

# Set up matrix equation
M = t.stack([-D, B - A, C - A], dim=-1)
b_vec = O - A

# Watch out for singular matrices
dets = t.linalg.det(M)
is_singular = dets.abs() < 1e-8
M[is_singular] = t.eye(3).to(device)

# Solve system for ALL ray-triangle pairs
sol = t.linalg.solve(M, b_vec)
s = sol[..., 0]   # shape: [nrays, ntriangles]
s *= D[..., 0]   # distance scaling

is_closest_triangle = (s == closest_distances.unsqueeze(-1))
closest_triangle_indices = is_closest_triangle.to(t.long).argmax(dim=-1) # shape: [nrays]
```

**3. Computing normal vectors for all the chosen triangles**

To find which way a flat triangle is facing, we pick two of its edges ($\vec{E_1}$ and $\vec{E_2}$) and compute their cross product. The cross product outputs a new vector that points perfectly perpendicular to both edges:

$$
\vec{N}_{\text{raw}} = \vec{E}_1 \times \vec{E}_2
$$

We then divide this vector by its own length to make it a unit vector (length of $1$):

$$
\vec{N} = \frac{\vec{N}_{\text{raw}}}{\|\vec{N}_{\text{raw}}\|}
$$

```python
edge1 = triangles[:, 1] - triangles[:, 0]
edge2 = triangles[:, 2] - triangles[:, 0]
normals = t.cross(edge1, edge2, dim=1) # Specify dim=1 so it doesn't crash
normals = normals / t.norm(normals, dim=1, keepdim=True)
```

**4. Normalize light vector and calculate intensities**

We calculate the dot product between our normalized surface normal $\vec{N}$ and our normalized light direction $\vec{L}$.If the triangle is facing away from the light, the dot product will be negative. Because things can't have "negative brightness," we use t.where to chop off any negative values and set them to 0.0.

$$
\text{Intensity} = \max(0, \vec{N} \cdot \vec{L})
$$

```python
light_normalized = light / t.norm(light)
intensity_per_triangle = t.einsum("nd, d -> n", normals, light_normalized)
intensity_per_triangle = t.where(intensity_per_triangle > 0, intensity_per_triangle, 0.0)
```

**5. Adding Ambient Light and rendering**

If a triangle is hidden in a shadow, it shouldn't be pitch black (otherwise, you couldn't see the shape of the object at all). We add a small baseline of constant light called ambient_intensity.

$$
\text{Final Color} = \text{Intensity} + \text{Ambient Intensity}
$$

Finally, the code checks if the ray actually hit something (closest_distances.isfinite()). If it did, it gives it the calculated brightness. If the ray missed everything and flew off into outer space, it returns 0.0 (pure black background).

```python
intensity_per_ray = intensity_per_triangle[closest_triangle_indices]
final_intensity = intensity_per_ray + ambient_intensity
final_intensity = t.where(closest_distances.isfinite(), final_intensity, 0.0)
```

---

## Full Code Solution

[Link to GitHub repo with my implementation](https://github.com/akshayavb99/ARENA_3.0/blob/main/chapter0_fundamentals/exercises/part1_ray_tracing/exercises.py)
