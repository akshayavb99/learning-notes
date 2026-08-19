---

title: Leetcode 286- Islands and Treasure
tags:

- leetcode
- neetcode-150-list
- python
- graph
- bfs
- multi-source-bfs
- deque
updated_date: 2026-08-19
url: https://neetcode.io/problems/islands-and-treasure

---

# Leetcode 286- Islands and Treasure

## Understanding the Problem

You are given an $m \times n$ grid filled with three types of values:

- `-1`: Water or an obstacle that cannot be traversed.
- `0`: A treasure chest.
- `2**31 - 1` (`INF`): Empty land.

The goal is to update each empty land cell with the distance to its nearest treasure chest. If an empty land cell cannot reach any treasure, its value remains `INF`.

## Solution Implementation

Instead of running individual BFS searches starting from every land cell (which would lead to duplicate work), we use a **Multi-Source Breadth-First Search (BFS)** starting simultaneously from all treasure positions (`0`).

1. **Initialize Queue:** Scan the grid and add all coordinates containing a treasure (`0`) into a `deque`.
2. **Multi-Source Expansion:** Pop coordinates from the queue one by one and explore their four adjacent neighbors (up, down, left, right).
3. **Update Distance:** If a neighboring cell is within bounds and contains `(2**31) - 1` (unvisited land), set its value to `current_cell_value + 1` and append its position to the queue.
4. **Shortest Path Property:** Because BFS expands outward layer-by-layer, the first time a land cell is reached, it is guaranteed to be via the shortest distance from *any* treasure.

### Code

```python
from collections import deque
from typing import List


class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        # Step 1: Add all treasure positions to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Directions: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Multi-source BFS outwards from all treasures simultaneously
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and ensure target is an unvisited land cell
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == (2-**31) - 1
                ):

                    # Update distance and enqueue
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

```

### Time Complexity

- $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns. Each grid cell is added to and removed from the queue at most once.

Overall time complexity is $O(m \times n)$.

### Space Complexity

- $O(m \times n)$ for the `deque` in the worst-case scenario where the entire grid is initially filled with treasure positions.

Overall space complexity is $O(m \times n)$.

## Additional Resources

- https://neetcode.io/problems/islands-and-treasure
- https://leetcode.com/problems/walls-and-gates/description/