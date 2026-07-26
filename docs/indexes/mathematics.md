---
title: Mathematics Index
tags:
  - mathematics
  - index
updated_date: 2026-07-26
---

# Mathematics Index

Notes and resources on distributed systems and system design.

## Linear Algebra Important Terms and Concepts

Here is a detailed breakdown of all 13 linear algebra concepts, expanded with formulas, examples, key properties, and trade-offs.

---

### Scalars

- **Definition:** Single real or complex numbers that scale vectors, having magnitude but no direction.
- **Formula:**

$$c \in \mathbb{R} \quad \text{or} \quad c \in \mathbb{C}$$

- **Example:** $c = -5$ or mass $m = 75 \text{ kg}$.
- **Properties:**
- Commutative under multiplication: $c \cdot d = d \cdot c$.
- Distributive over vector addition: $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$.

- **Advantages:** Extremely simple to store and compute; acts as the fundamental scaling factor in linear transformations.
- **Disadvantages:** Cannot encode multidimensional information, directional spatial data, or complex systems on its own.

---

### Vectors

- **Definition:** Ordered arrays of numbers that represent points or direction and magnitude in a vector space.
- **Formula:**

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

- **Example:** Position in 2D space $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$.

- **Properties:**
- Added element-wise: $\mathbf{u} + \mathbf{v} = [u_1 + v_1, \dots, u_n + v_n]^T$.
- Euclidean length/norm is given by $\Vert{}\mathbf{v}\Vert{} = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$.

- **Advantages:** Compactly stores directional quantities, multi-feature data points, and state vectors.
- **Disadvantages:** Operations become computationally expensive as dimension $n$ grows very large (curse of dimensionality).

---

### Matrices

- **Definition:** Two-dimensional rectangular arrays of numbers arranged in rows and columns.
- **Formula:**

$$A = (a_{ij}) \in \mathbb{R}^{m \times n} = \begin{bmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{bmatrix}$$

- **Example:** $A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$.
- **Properties:**
- Represents linear transformations mapping $\mathbb{R}^n \to \mathbb{R}^m$.
- Transpose swaps rows and columns: $(A^T)_{ij} = A_{ji}$.

- **Advantages:** Allows massive parallel linear equations to be solved efficiently using matrix algebra.
- **Disadvantages:** Dense matrix storage scales quadratically $O(m \times n)$, leading to memory bottlenecks for large systems.

---

### Tensors

- **Definition:** Multidimensional generalization of scalars, vectors, and matrices to higher dimensions.
- **Formula:**

$$\mathcal{T} \in \mathbb{R}^{n_1 \times n_2 \times \dots \times n_d}$$

- **Example:** An RGB image tensor of size $1920 \times 1080 \times 3$ (Height $\times$ Width $\times$ Channels).
- **Properties:**
- Order/Rank $d$ indicates the number of indexing axes required.
- Can be reshaped, flattened, or contracted across indices.

- **Advantages:** Essential for multi-way data representation, deep learning, continuum mechanics, and general relativity.
- **Disadvantages:** High-order tensor decompositions are computationally complex and difficult to visualize directly.

---

### Vector Spaces

- **Definition:** Sets of vectors that are closed under vector addition and scalar multiplication, satisfying specific algebraic axioms.
- **Formula:**

$$V = \{ \mathbf{v} \mid \forall \mathbf{u}, \mathbf{v} \in V, \, c \in \mathbb{R} \implies (\mathbf{u} + \mathbf{v}) \in V \text{ and } (c\mathbf{v}) \in V \}$$

- **Example:** The set of all 3D real vectors $\mathbb{R}^3$, or the space of all continuous functions $C[a, b]$.
- **Properties:**
- Contains a unique zero vector $\mathbf{0}$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$.
- Every vector $\mathbf{v}$ has an additive inverse $-\mathbf{v}$.

- **Advantages:** Provides a unified theoretical framework that unifies geometry, systems of equations, and functional analysis.
- **Disadvantages:** Abstract vector spaces (like infinite-dimensional spaces) require sophisticated analysis to manage convergence and bounds.

---

### Subspaces

- **Definition:** Subsets of a vector space that are themselves valid vector spaces under the same addition and scalar multiplication operations.
- **Formula:**

$$W \subseteq V \quad \text{where} \quad \mathbf{0} \in W, \; \mathbf{u}+\mathbf{v} \in W, \; c\mathbf{v} \in W$$

- **Example:** A line or plane passing through the origin in $\mathbb{R}^3$.
- **Properties:**
- Must contain the origin $\mathbf{0}$.
- Intersection of two subspaces is always a subspace.

- **Advantages:** Reduces problem size by restricting analysis to lower-dimensional invariant regions.
- **Disadvantages:** Subspaces that do not pass through the origin are not closed under operations (forming affine spaces instead).

---

### Linear Combinations

- **Definition:** Expressions formed by multiplying vectors by scalar coefficients and summing the resulting terms.
- **Formula:**

$$\mathbf{w} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \sum_{i=1}^{k} c_i \mathbf{v}_i$$

- **Example:** $\begin{bmatrix} 5 \\ 7 \end{bmatrix} = 5\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 7\begin{bmatrix} 0 \\ 1 \end{bmatrix}$.
- **Properties:**
- Maps a vector of coefficients directly to a target destination in the vector space.
- Linear operators preserve linear combinations: $T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})$.

- **Advantages:** Forms the foundational building block for constructing spaces, approximations, and transforms.
- **Disadvantages:** Small changes in scalar coefficients can lead to large errors if vectors are nearly parallel.

---

### Span

- **Definition:** The set of all possible linear combinations that can be formed from a given collection of vectors.
- **Formula:**

$$\operatorname{Span}(\mathbf{v}_1, \dots, \mathbf{v}_k) = \left\{ \sum_{i=1}^{k} c_i \mathbf{v}_i \;\middle\vert{}\; c_i \in \mathbb{R} \right\}$$

- **Example:** $\operatorname{Span}\left(\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}\right)$ is the entire xy-plane in $\mathbb{R}^3$.
- **Properties:**
- Always forms a valid subspace of the parent vector space.
- Adding redundant vectors to the set does not expand the spanned space.

- **Advantages:** Identifies the complete reachable subspace using a discrete set of generator vectors.
- **Disadvantages:** A spanning set may contain redundant vectors, making representation inefficient unless minimized.

---

### Basis

- **Definition:** A linearly independent set of vectors that spans an entire vector space.
- **Formula:**

$$\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\} \quad \text{such that } \operatorname{Span}(\mathcal{B}) = V \text{ and } \mathcal{B} \text{ is linearly independent}$$

- **Example:** The standard basis for $\mathbb{R}^2$ is $\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix}\right\}$.
- **Properties:**
- Every vector in $V$ can be expressed as a unique linear combination of basis vectors.
- Bases are non-unique; a vector space has infinitely many choices of basis.

- **Advantages:** Provides a minimal, non-redundant coordinate framework to represent any element in the space.
- **Disadvantages:** Changing coordinates between different non-orthogonal bases requires matrix inversions.

---

### Dimension

- **Definition:** The maximum number of linearly independent vectors in a vector space, equal to the number of vectors in any of its bases.
- **Formula:**

$$\dim(V) = \vert{}\mathcal{B}\vert{}$$

- **Example:** $\dim(\mathbb{R}^n) = n$, so $\dim(\mathbb{R}^3) = 3$.
- **Properties:**
- If $W$ is a subspace of $V$, then $\dim(W) \le \dim(V)$.
- Any set of $\dim(V)$ linearly independent vectors automatically forms a basis for $V$.

- **Advantages:** Gives a precise topological measure of the degrees of freedom within a space.
- **Disadvantages:** Infinite-dimensional spaces (e.g., function spaces) require special analytical techniques like Hilbert space norms.

---

### Linear Independence

- **Definition:** A property of a set of vectors where no vector in the set can be expressed as a linear combination of the others.
- **Formula:**

$$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \dots = c_k = 0$$

- **Example:** The vectors $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ are independent; $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\begin{bmatrix} 2 \\ 4 \end{bmatrix}$ are dependent.
- **Properties:**
- A set containing the zero vector $\mathbf{0}$ is automatically linearly dependent.
- Determinant of a square matrix made of these vectors is non-zero ($\det(A) \neq 0$).

- **Advantages:** Eliminates redundant data and guarantees unique solutions for linear systems.
- **Disadvantages:** Checking independence on noisy real-world data is prone to numerical instability (near dependency).

---

### Matrix Representation

- **Definition:** The encoding of a linear transformation using a grid of numbers corresponding to a chosen basis.
- **Formula:**

$$[T]_{\mathcal{B}} = \begin{bmatrix} [T(\mathbf{b}_1)]_{\mathcal{B}} & [T(\mathbf{b}_2)]_{\mathcal{B}} & \dots & [T(\mathbf{b}_n)]_{\mathcal{B}} \end{bmatrix}$$

- **Example:** A $90^\circ$ counterclockwise 2D rotation matrix is $R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.
- **Properties:**
- Depends directly on the choice of domain and codomain bases.
- Composition of transformations maps to matrix multiplication: $[T \circ S] = [T][S]$.

- **Advantages:** Turns abstract geometric or operational transformations into simple arithmetic operations.
- **Disadvantages:** Requires basis change transformations when operating between different coordinate frames.

---

### Matrix Multiplication

- **Definition:** An operation combining two matrices by taking the dot products of the first matrix's rows with the second matrix's columns.
- **Formula:**

$$C = AB \quad \text{where} \quad c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

- **Example:**

$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 1(5) + 2(6) \\ 3(5) + 4(6) \end{bmatrix} = \begin{bmatrix} 17 \\ 39 \end{bmatrix}$$

- **Properties:**
- Associative: $A(BC) = (AB)C$.
- Non-commutative in general: $AB \neq BA$.

- **Advantages:** Allows sequential transformations to be combined into a single operator matrix.
- **Disadvantages:** Standard algorithm has an expensive computational complexity of $O(n^3)$.

---

Here is a detailed breakdown of these linear algebra terms, formulas, examples, properties, and trade-offs:

---

### Dot Product

- **Definition:** An algebraic operation that takes two equal-length sequences of numbers and returns a single scalar by summing the products of corresponding entries.
- **Formula:**

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = \Vert{}\mathbf{u}\Vert{}_2 \Vert{}\mathbf{v}\Vert{}_2 \cos\theta$$

- **Example:**

$$\begin{bmatrix} 1 \\ 2 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 4 \end{bmatrix} = (1 \times 3) + (2 \times 4) = 11$$

- **Properties:**
- Commutative: $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$.
- Distributive over addition: $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$.

- **Advantages:** Computationally fast ($O(n)$ complexity) and directly connects geometry (angles) to algebra.
- **Disadvantages:** Restricted strictly to real Euclidean spaces $\mathbb{R}^n$ (unlike general inner products).

---

### Inner Product

- **Definition:** A generalization of the dot product to abstract vector spaces that maps two vectors to a scalar satisfying symmetry, linearity, and positive-definiteness.
- **Formula:**

$$\langle \mathbf{u}, \mathbf{v} \rangle \quad \text{e.g., for functions } f, g: \quad \langle f, g \rangle = \int_{a}^{b} f(x) g(x) \, dx$$

- **Example:** Standard inner product in $\mathbb{R}^n$ is the dot product; for polynomials $p(x) = x, q(x) = x^2$ on $[0, 1]$, $\langle p, q \rangle = \int_{0}^{1} x^3 \, dx = \frac{1}{4}$.
- **Properties:**
- Positive definite: $\langle \mathbf{v}, \mathbf{v} \rangle \ge 0$, and $\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$.
- Conjugate symmetric: $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$.

- **Advantages:** Establishes geometric concepts (length, distance, orthogonality) in complex and infinite-dimensional spaces.
- **Disadvantages:** Computing abstract inner products (e.g., continuous integrals) can be computationally intensive.

---

### Outer Product

- **Definition:** An operation that takes two vectors and produces a matrix consisting of all possible pairwise products of their components.
- **Formula:**

$$\mathbf{u} \otimes \mathbf{v} = \mathbf{u} \mathbf{v}^T = \begin{bmatrix} u_1 v_1 & u_1 v_2 & \cdots & u_1 v_n \\ u_2 v_1 & u_2 v_2 & \cdots & u_2 v_n \\ \vdots & \vdots & \ddots & \vdots \\ u_m v_1 & u_m v_2 & \cdots & u_m v_n \end{bmatrix}$$

- **Example:**

$$\begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 3 & 4 \end{bmatrix} = \begin{bmatrix} 3 & 4 \\ 6 & 8 \end{bmatrix}$$

- **Properties:**
- The resulting matrix $\mathbf{u} \mathbf{v}^T$ always has a rank of at most $1$.
- Non-commutative: $\mathbf{u} \mathbf{v}^T \neq \mathbf{v} \mathbf{u}^T$.

- **Advantages:** Essential for low-rank matrix approximations, neural network weight updates, and covariance calculations.
- **Disadvantages:** Expands space significantly by increasing dimension from $O(n)$ storage to $O(m \times n)$.

---

### L1 Norm

- **Definition:** A vector norm defined as the sum of the absolute values of the vector components, measuring distance along grid axes.
- **Formula:**

$$\Vert{}\mathbf{x}\Vert{}_1 = \sum_{i=1}^{n} \vert{}x_i\vert{}$$

- **Example:**

$$\left\Vert{} \begin{bmatrix} 3 \\ -4 \end{bmatrix} \right\Vert{}_1 = \vert{}3\vert{} + \vert{}-4\vert{} = 7$$

- **Properties:**
- Unit ball takes the shape of a diamond or cross-polytope.
- Satisfies subadditivity (triangle inequality): $\Vert{}\mathbf{x} + \mathbf{y}\Vert{}_1 \le \Vert{}\mathbf{x}\Vert{}_1 + \Vert{}\mathbf{y}\Vert{}_1$.

- **Advantages:** Promotes sparsity in optimization models (e.g., Lasso regularization) and is robust to extreme outliers.
- **Disadvantages:** Non-differentiable at zero, making gradient-based optimization trickier.

---

### L2 Norm

- **Definition:** The standard Euclidean norm measuring the straight-line length of a vector from the origin.
- **Formula:**

$$\Vert{}\mathbf{x}\Vert{}_2 = \sqrt{\sum_{i=1}^{n} x_i^2} = \sqrt{\mathbf{x}^T \mathbf{x}}$$

- **Example:**

$$\left\Vert{} \begin{bmatrix} 3 \\ -4 \end{bmatrix} \right\Vert{}_2 = \sqrt{3^2 + (-4)^2} = 5$$

- **Properties:**
- Rotationally invariant (length remains unchanged under rotation).
- Strictly convex and smooth everywhere.

- **Advantages:** Smoothly differentiable everywhere, making it ideal for gradient descent loss functions.
- **Disadvantages:** Sensitive to severe outliers because squaring large errors amplifies their weight.

---

### Infinity Norm

- **Definition:** A norm that returns the maximum absolute magnitude among all individual components of a vector.
- **Formula:**

$$\Vert{}\mathbf{x}\Vert{}_\infty = \max_{1 \le i \le n} \vert{}x_i\vert{}$$

- **Example:**

$$\left\Vert{} \begin{bmatrix} -5 \\ 2 \\ 4 \end{bmatrix} \right\Vert{}_\infty = \max(\vert{}-5\vert{}, \vert{}2\vert{}, \vert{}4\vert{}) = 5$$

- **Properties:**
- Serves as the limit of the $L_p$ norm as $p \to \infty$.
- Unit ball forms a hypercube.

- **Advantages:** Extremely fast to calculate since it requires no multiplications or square root operations.
- **Disadvantages:** Discards overall signal structure by focusing exclusively on a single peak entry.

---

### Frobenius Norm

- **Definition:** A matrix norm defined as the square root of the sum of the absolute squares of all its elements.
- **Formula:**

$$\Vert{}A\Vert{}_F = \sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n} \vert{}a_{ij}\vert{}^2} = \sqrt{\operatorname{Tr}(A^T A)}$$

- **Example:**

$$\left\Vert{} \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix} \right\Vert{}_F = \sqrt{1^2 + 2^2 + 2^2 + 1^2} = \sqrt{10}$$

- **Properties:**
- Invariant under unitary transformations: $\Vert{}U A V\Vert{}_F = \Vert{}A\Vert{}_F$.
- Sub-multiplicative: $\Vert{}A B\Vert{}_F \le \Vert{}A\Vert{}_F \Vert{}B\Vert{}_F$.

- **Advantages:** Simple generalization of the vector $L_2$ norm to matrices; easy to differentiate in matrix calculus.
- **Disadvantages:** Treats matrices as flat arrays of numbers, ignoring spectral or operator properties.

---

### Euclidean Distance

- **Definition:** The length of the straight line segment connecting two points in Euclidean space.
- **Formula:**

$$d(\mathbf{x}, \mathbf{y}) = \Vert{}\mathbf{x} - \mathbf{y}\Vert{}_2 = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$

- **Example:** Distance between $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\begin{bmatrix} 4 \\ 6 \end{bmatrix}$ is $\sqrt{(1-4)^2 + (2-6)^2} = 5$.
- **Properties:**
- Symmetric: $d(\mathbf{x}, \mathbf{y}) = d(\mathbf{y}, \mathbf{x})$.
- Obeys triangle inequality: $d(\mathbf{x}, \mathbf{z}) \le d(\mathbf{x}, \mathbf{y}) + d(\mathbf{y}, \mathbf{z})$.

- **Advantages:** Highly intuitive spatial metric reflecting physical real-world distances.
- **Disadvantages:** Performance degrades in very high dimensions due to the curse of dimensionality (distances concentrate).

---

### Manhattan Distance

- **Definition:** The distance between two points measured along axes at right angles, representing grid-based paths.
- **Formula:**

$$d(\mathbf{x}, \mathbf{y}) = \Vert{}\mathbf{x} - \mathbf{y}\Vert{}_1 = \sum_{i=1}^{n} \vert{}x_i - y_i\vert{}$$

- **Example:** Distance between $(1, 2)$ and $(4, 6)$ is $\vert{}1-4\vert{} + \vert{}2-6\vert{} = 3 + 4 = 7$.
- **Properties:**
- Measures distance along orthogonal grid lines (Taxicab metric).
- Scale-dependent across dimensions.

- **Advantages:** Less impacted by extreme single-dimension outliers compared to Euclidean distance.
- **Disadvantages:** Non-unique shortest paths; sensitive to coordinate system rotations.

---

### Cosine Distance

- **Definition:** A metric measuring the angular divergence between two non-zero vectors, independent of their lengths.
- **Formula:**

$$d_{\text{cos}}(\mathbf{x}, \mathbf{y}) = 1 - \frac{\mathbf{x} \cdot \mathbf{y}}{\Vert{}\mathbf{x}\Vert{}_2 \Vert{}\mathbf{y}\Vert{}_2}$$

- **Example:** For collinear vectors $\mathbf{x} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\mathbf{y} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$, $d_{\text{cos}}(\mathbf{x}, \mathbf{y}) = 1 - 1 = 0$.
- **Properties:**
- Bounded between $0$ (identical direction) and $2$ (opposite direction).
- Invariant to scalar positive scaling: $d_{\text{cos}}(c\mathbf{x}, \mathbf{y}) = d_{\text{cos}}(\mathbf{x}, \mathbf{y})$ for $c > 0$.

- **Advantages:** Excellent for text analysis and high-dimensional sparse data where magnitude matters less than topic orientation.
- **Disadvantages:** Is not a strict metric space distance (violates the triangle inequality).

---

### Orthogonality

- **Definition:** The condition where two vectors meet at right angles, resulting in a zero inner product.
- **Formula:**

$$\mathbf{u} \cdot \mathbf{v} = 0 \quad \iff \quad \mathbf{u} \perp \mathbf{v}$$

- **Example:**

$$\begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix} = 1(0) + 0(1) = 0$$

- **Properties:**
- Non-zero orthogonal vectors are automatically linearly independent.
- Obeys the generalized Pythagorean theorem: $\Vert{}\mathbf{u} + \mathbf{v}\Vert{}^2 = \Vert{}\mathbf{u}\Vert{}^2 + \Vert{}\mathbf{v}\Vert{}^2$.

- **Advantages:** Decouples variables, eliminating cross-talk and drastically simplifying calculations and projections.
- **Disadvantages:** Gram-Schmidt orthogonalization needed to build orthogonal sets can suffer from numerical instability.

---

### Orthogonal Projection

- **Definition:** The linear mapping of a vector onto a subspace such that the difference vector is orthogonal to that subspace.
- **Formula:**

$$\operatorname{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{u}}{\Vert{}\mathbf{u}\Vert{}_2^2} \mathbf{u} \quad \text{or for matrix } A: \quad P = A (A^T A)^{-1} A^T$$

- **Example:** Projecting $\begin{bmatrix} 3 \\ 4 \end{bmatrix}$ onto the horizontal axis $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ yields $\begin{bmatrix} 3 \\ 0 \end{bmatrix}$.
- **Properties:**
- Idempotent: $P^2 = P$ (projecting a second time changes nothing).
- Symmetric: $P^T = P$.

- **Advantages:** Finds the unique best lower-dimensional linear approximation under least squares criteria.
- **Disadvantages:** Computing $(A^T A)^{-1}$ for large dense matrices is computationally expensive and potentially ill-conditioned.

---

- \[Gram-Schmidt process]
- Rank
- Null space
- Column space, Row space
- Matrix inverse
- Determinant
- Trace
- Symmetric matrices
- Positive definite matrices
- Eigenvalue, Eigenvectors
- Eigen decomposition
  - \[Singular Value Decomposition]
  - \[Low-rank approximation]
  - \[Matrix factorization]

## Calculus Important Terms and Concepts

- Functions
- Limits
- Derivatives
- Partial derivatives
- Directional derivatives
- Gradient, Gradient vector
- Chain rule
- Multivariate calculus
- Jacobian matrix, Hessian matrix
- Taylor approximation
- First-order approximation, Second-order approximation
- Automatic differentiation
- Computational graphs
- Symbolic differentiation
- Numerical differentiation
- Backpropagation foundations

## Probability Theory Important Terms and Concepts

- Probability axioms
- Events
- Random variables
- Discrete random variables
- Continuous random variables
- Probability mass function
- Probability density function
- Cumulative distribution function
- Conditional probability
- Joint probability
- Marginal probability
- Bayes theorem
- Independence
- Conditional independence
- Expectation
- Variance
- Covariance
- Moments
- Common distributions (Gaussian distribution, Bernoulli distribution, Binomial distribution, Multinomial distribution, Poisson distribution, Exponential distribution, Uniform distribution)
- Law of large numbers
- Central limit theorem
- Maximum likelihood estimation
- Maximum a posteriori estimation
- Bayesian inference
- Markov chains

## Statistics Important Terms and Concepts

- Descriptive statistics
- Mean
- Median
- Mode
- Variance
- Standard deviation
- Sampling
- Sampling bias
- Population vs sample
- Estimation
- Confidence intervals
- Hypothesis testing
- Null hypothesis
- Alternative hypothesis
- P-value
- Statistical significance
- Statistical power
- Multiple hypothesis testing
- Correlation
- Covariance
- Causation
- Experimental design
- A/B testing
