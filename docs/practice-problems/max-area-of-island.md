---
title: Leetcode 695 - Max Area of Island
tags:
  - leetcode
  - neetcode-150-list
  - python
  - dfs
  - graph
updated_date: 2026-07-20
url: https://leetcode.com/problems/max-area-of-island/
---

# Leetcode 695 - Max Area of Island

## Understanding the Problem

The goal is to find the **largest connected group of land cells** in a binary matrix. Each cell contains either:

- `1` → Land
- `0` → Water

An island consists of horizontally and vertically adjacent land cells. The task is to compute the maximum number of cells belonging to any single island.

A natural approach is to perform **Depth-First Search (DFS)** from every unvisited land cell. DFS explores all connected land cells before returning, allowing us to calculate the total area of an island.

- **State Tracking:** A `seen` set stores the coordinates of cells that have already been visited. This prevents revisiting cells and avoids infinite recursion.
- **Base Cases:** DFS immediately returns `0` when:
  1. The current cell is outside the grid boundaries.
  2. The current cell is water (`0`).
  3. The current cell has already been visited.
- **Area Calculation:** Every valid land cell contributes `1` to the island's area. The total area is obtained by recursively exploring all four neighboring directions (up, down, left, right) and summing their contributions.
- **Global Maximum:** After each DFS traversal, compare the computed island area with the current maximum area.

---

## Solution Implementation

### Code

```python
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0 or
                (r, c) in seen
            ):
                return 0

            seen.add((r, c))

            return (
                1
                + dfs(r - 1, c)
                + dfs(r + 1, c)
                + dfs(r, c - 1)
                + dfs(r, c + 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    max_area = max(max_area, dfs(r, c))

        return max_area
```

### Time Complexity

Each cell in the grid is visited at most once. During the DFS traversal, every land cell is marked as visited and never explored again. Each recursive call performs only constant-time work besides visiting neighboring cells.

For a grid with `m` rows and `n` columns:

**Overall time complexity — $O(m \times n)$**

### Space Complexity

- **Visited Set:** Stores every land cell at most once, requiring up to $O(m \times n)$ space.
- **Recursion Stack:** In the worst case (the entire grid is one island), the recursion depth can reach $O(m \times n)$.

**Overall space complexity — $O(m \times n)$**

---

## Key Takeaways

- DFS is well-suited for exploring connected components in a grid.
- Mark cells as visited immediately after entering them to avoid revisiting.
- The area of an island is computed by **summing** the results from all four recursive calls—not taking the maximum.
- Every cell should be visited at most once, giving a linear-time solution.

---

## Additional Resources

- https://neetcode.io/problems/max-area-of-island
- https://leetcode.com/problems/max-area-of-island/
