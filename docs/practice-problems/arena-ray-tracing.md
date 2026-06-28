---
title: ARENA - 0.1 Ray Tracing
description: |
  My notes and explanation about the exercises for Ray Tracing Exercises in the ARENA curriculum
tags:
  - pytorch
  - numpy
  - linear-algebra
updated_date: 2026-06-28
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

## Full Code Solution

[Link to GitHub repo with my implementation](https://github.com/akshayavb99/ARENA_3.0/blob/main/chapter0_fundamentals/exercises/part1_ray_tracing/exercises.py)
