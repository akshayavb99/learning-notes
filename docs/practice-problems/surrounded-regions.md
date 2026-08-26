---
title: Leetcode 130 - Surrounding Regions
tags:
    - leetcode
    - neetcode-150-list
    - python
    - dfs
    - matrix
    - graph
updated_date: 2026-08-26
url: https://leetcode.com/problems/surrounded-regions/
---

# Leetcode 130 - Surrounding Regions

## Understanding the Problem

Given an $m \times n$ matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally **surrounded by `'X'**`.

Rules for capturing:

- A cell `'O'` is **surrounded** if none of the `'O'` cells in its connected region touch the outer boundary of the grid.
- A connected region of `'O'`s touching any boundary cell (top, bottom, left, right) **cannot be surrounded** and must remain `'O'`.
- All other `'O'` regions must be flipped to `'X'` in-place.

---

# Key Data Structures

## 1. Implicit Call Stack (Recursion)

Depth-First Search (DFS) uses Python's call stack to traverse all connected `'O'` cells starting from the boundary.

## 2. In-Place Temporary Markers (`'T'`)

Instead of using a separate `visited` matrix to keep track of safe cells, we mutate uncaptured `'O'` cells directly to a temporary character `'T'` during traversal.

---

# Optimal Approach Intuition

Rather than scanning from the inside to see if an `'O'` region reaches a boundary, **reverse the problem**:

> Any `'O'` located on the border of the board (and any `'O'` connected to it) **cannot** be captured.

By starting our traversal strictly from border `'O'`s and marking them as temporary safe spots (`'T'`), every remaining `'O'` in the interior is guaranteed to be completely surrounded.

---

# Why Reverse Traversal (Border-First DFS)?

## 1. Direct Region Checking is Complex

Starting from an interior `'O'` requires traversing the entire component first to verify whether *any* connected cell hits the border. If it does hit a border late in the traversal, you have to backtrack or re-traverse to un-flip them.

## 2. Boundary Propagation is Definitive

Border `'O'`s are unconditionally safe. Traversing outward from the boundaries guarantees we label all non-capturable cells upfront in a single pass before modifying the rest of the board.

---

# How the Optimal Approach Works

## Step 1: Boundary DFS Sweep

Iterate along all four borders (top, bottom, left, right rows and columns). Whenever an `'O'` is found on the border, run a recursive `capture(r, c)` DFS to mark that cell and all contiguous `'O'` neighbors as `'T'`.

```
Board (Initial):          After Border DFS:
X  X  X  X                X  X  X  X
X  O  O  X    ========>   X  O  O  X
X  X  O  X                X  X  O  X
X  O  X  X                X  T  X  X

```

---

## Step 2: Full Matrix Scan & Mutation

Iterate through every cell in the matrix $R \times C$:

- If `board[r][c] == 'O'`: It was never reached from the border. Flip it to `'X'`.
- If `board[r][c] == 'T'`: It is connected to a border. Restore it back to `'O'`.

```
After Step 1:             Final State:
X  X  X  X                X  X  X  X
X  O  O  X    ========>   X  X  X  X
X  X  O  X                X  X  X  X
X  T  X  X                X  O  X  X

```

---

# Solution Implementation

```python
from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        R, C = len(board), len(board[0])

        # Capture unsurrounded regions (O -> T)
        def capture(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != "O":
                return

            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Run DFS for border cells in first & last rows
        for c in range(C):
            capture(0, c)
            capture(R - 1, c)

        # Step 1 (cont): Run DFS for border cells in first & last columns
        for r in range(R):
            capture(r, 0)
            capture(r, C - 1)

        # Step 2: Flip captured 'O' to 'X', and restore 'T' back to 'O'
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

```

---

# Complexity Analysis

Let:

- $R$ = number of rows in the matrix
- $C$ = number of columns in the matrix

## Time Complexity: $O(R \times C)$

- **Border Search & DFS:** Every cell is visited at most a constant number of times during the boundary DFS traversals.
- **Final Grid Scan:** A single pass over all $R \times C$ cells updates the characters in place.

**Overall Time Complexity: $O(R \times C)$**

---

## Space Complexity: $O(R \times C)$

- **Call Stack:** In the worst-case scenario (e.g., an entire grid of `'O'`s), the maximum recursive call stack depth can reach $O(R \times C)$.
- **In-place Grid Modification:** Uses $O(1)$ auxiliary memory by mutating the grid directly with `'T'` as a temporary marker.

**Overall Space Complexity: $O(R \times C)$**

---

# Key Takeaways

- **Complementary Thinking:** Instead of finding which interior nodes meet the conditions to be captured, find the boundary nodes that are immune to being captured.
- **Temporary State Marking:** Mutating matrix elements to temporary values (like `'T'`) eliminates the space overhead of a separate `visited` set or matrix.
- **In-Place Transformation:** Returning `None` and updating the matrix directly satisfies strict $O(1)$ space constraints outside of recursion stack costs.

---

# Common Mistakes

## Mistake 1: Stack Overflow on Large Grids

Using deep recursion on large inputs can cause a `RecursionError` in Python if the recursion limit is exceeded.

Fix:

* Use an iterative BFS or explicit stack-based DFS with a loop if maximum grid dimensions are extremely large.

---

## Mistake 2: Forgetting Board Corners

Checking borders by iterating rows and columns separately can accidentally miss corner cases or apply duplicate checks if bounds aren't written carefully.

Fix:

* Keep boundary sweeps simple by running `capture(r, c)` on every border row `0`, `R-1` and column `0`, `C-1`.

---

## Mistake 3: Overwriting Unvisited 'O's Too Early

Flipping `'O'` to `'X'` during the boundary traversal instead of using a temporary marker `'T'` will permanently lose track of valid safe regions connected deeper inside the board.

Fix:

* Use a 3-step lifecycle: `'O'` (unvisited) $\rightarrow$ `'T'` (border-connected safe) $\rightarrow$ final flip pass.

---

# Additional Resources

* https://neetcode.io/problems/surrounded-regions
* https://leetcode.com/problems/surrounded-regions/