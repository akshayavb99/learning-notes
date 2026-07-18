---
title: Deep-ML - Matrix-Vector Dot Product
tags:
  - deep-ml
  - linear-algebra
  - python
  - matrix-operations
updated_date: 2026-07-16
url: https://www.deep-ml.com/problems/1
---

# Deep-ML 1 - Matrix-Vector Dot Product

## Understanding the Problem

The goal is to compute the result of multiplying a matrix $A$ by a vector $v$. This operation is fundamental in linear algebra and forms the core of many machine learning algorithms.

To perform matrix-vector multiplication, a crucial dimension compatibility rule must be satisfied: the number of **columns** in matrix $A$ must equal the number of **elements** in vector $v$. If this condition is not met, the operation is undefined.

- **Dimension Validation:** We first check if the length of the first row of matrix `a` matches the length of vector `b`. If they do not match, we return `-1`.
- **Dot Product Calculation:** For each row in matrix `a`, we calculate the dot product with vector `b`. The dot product is the sum of the products of the corresponding elements:
  $$c_i = \sum_{j=1}^{n} a_{ij} \cdot b_j$$
- **Result Accumulation:** Each calculated scalar value becomes an element in the resulting output list, matching the number of rows in matrix `a`.

---

## Solution Implementation

### Code

```python
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    # If the number of columns in 'a' does not match the length of 'b', return -1
    if len(a[0]) != len(b):
        return -1

    # Initialize the result list with zeros for each row of matrix 'a'
    result = [0] * len(a)

    # Iterate through each row of the matrix
    for i, row in enumerate(a):
        # Compute the dot product of the current row and the vector
        result[i] = sum([row[j] * b[j] for j in range(len(b))])

    return result
```

### Time Complexity

Let $m$ be the number of rows in matrix `a`, and $n$ be the number of columns in matrix `a` (which is equal to the length of vector `b`).

The algorithm iterates through all $m$ rows. For each row, it performs a list comprehension that executes element-wise multiplication and summation over $n$ elements.

**Overall time complexity — $O(m \cdot n)$**

### Space Complexity

- **Auxiliary Space:** The algorithm operates directly on the inputs using simple loop variables and list comprehensions without creating large intermediate data structures.
- **Output Space:** The `result` list stores $m$ elements, representing the height of the transformation.

**Overall space complexity — $O(m)$** _(including the space required to store the final output)_

---

## Additional Resources

- https://www.deep-ml.com/problems/1
- https://en.wikipedia.org/wiki/Matrix_multiplication
