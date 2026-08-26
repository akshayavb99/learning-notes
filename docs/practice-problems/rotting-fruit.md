---
title: Leetcode 994 - Rotting Oranges
tags:

- leetcode
- neetcode-150-list
- python
- bfs
- matrix
- graph
updated_date: 2026-08-20
url: https://leetcode.com/problems/rotting-oranges/
---

# Leetcode 994 - Rotting Oranges

## Understanding the Problem

The goal is to determine the minimum number of minutes needed until no fresh orange remains in an $m \times n$ grid.

Grid values represent:

- `0`: Empty cell
- `1`: Fresh orange
- `2`: Rotten orange

Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right) to a rotten orange becomes rotten.

Return:

- The minimum number of minutes that must elapse until no cell has a fresh orange.
- `-1` if it is impossible to rot all fresh oranges.

---

# Key Data Structures

## 1. Queue (`collections.deque`)

Stores the coordinates `(r, c)` of rotten oranges. A double-ended queue allows efficient $O(1)$ pops from the left and appends to the right for Breadth-First Search (BFS).

## 2. Fresh Counter (`fresh_count`)

Tracks the remaining number of fresh oranges. This avoids rescanning the entire grid at the end to check if any fresh oranges survived.

## 3. Direction Vectors

A list of coordinate offsets `[(1,0), (-1,0), (0,1), (0,-1)]` used to explore the 4-directional neighbors of a grid cell efficiently.

---

# Optimal Approach Intuition

Rotting happens **simultaneously** from all rotten oranges at every step. This makes **Multi-Source Breadth-First Search (BFS)** the ideal choice.

> Rather than starting BFS from one rotten orange at a time, we enqueue **all initial rotten oranges at time $T = 0$**.

Each level of the BFS represents 1 minute of time passing across the entire grid.

---

# Why Not DFS or Single-Source BFS?

## 1. DFS (Depth-First Search) Fails on Shortest Path

DFS explores as far down a path as possible before backtracking. It does not naturally model time passing in uniform, 1-minute steps across multiple sources.

## 2. Independent BFS Iterations Are Redundant

Running BFS independently from each rotten orange requires overlapping work and extra tracking matrices to find the minimum distance from any rotten orange to a fresh orange.

Multi-source BFS handles all rot propagation in a single unified traversal.

---

# How the Optimal Approach Works

## Step 1: Initialize Queue and Count Fresh Oranges

Scan the grid once:

- Add every initial rotten orange `(r, c)` to the queue.
- Count the total number of fresh oranges (`fresh_count`).

```
Grid:
2  1  1
1  1  0
0  1  1

Initial Queue: [(0,0)]
fresh_count: 6

```

---

## Step 2: Level-Order Traversal (1 Level = 1 Minute)

Before processing a wave of rot, take a snapshot of the current queue length `len(q)`. This ensures we only process the oranges that are rotten at the current minute.

For each rotten orange in the current level:

1. Check its 4 neighbors.
2. If a neighbor is fresh (`1`), convert it to rotten (`2`).
3. Decrement `fresh_count` by 1.
4. Add the newly rotten orange to the queue for the next minute's wave.

---

## Step 3: Increment Time conditionally

Only increment `time += 1` after completing a full level **if fresh oranges were actually rotted**.

Stop the traversal when either:

- The queue becomes empty.
- `fresh_count` reaches 0.

---

# Solution Implementation

```python
from collections import deque
from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_count = 0
        time = 0

        rows, cols = len(grid), len(grid[0])

        # Step 1: Collect initial rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Multi-source BFS
        while q and fresh_count > 0:
            level_size = len(q)

            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check boundaries and fresh status
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr, nc))

            time += 1

        # Step 3: Return result based on remaining fresh oranges
        return time if fresh_count == 0 else -1

```

---

# Complexity Analysis

Let:

- $M$ = number of rows in the grid
- $N$ = number of columns in the grid

## Time Complexity: $O(M \times N)$

- **Grid scan:** $O(M \times N)$ to find initial state.
- **BFS Traversal:** Each cell is enqueued at most once and visited up to 4 times (for boundary/neighbor checks).

**Overall Time Complexity: $O(M \times N)$**

---

## Space Complexity: $O(M \times N)$

- **Queue Storage:** In the worst-case scenario (e.g., all cells are filled with rotten oranges), the queue holds up to $M \times N$ coordinates.
- **In-place Grid Modification:** Modifying the grid directly avoids needing an explicit `visited` set.

**Overall Space Complexity: $O(M \times N)$**

---

# Key Takeaways

- **Multi-Source BFS Pattern:** Whenever a process expands simultaneously from multiple starting points, enqueue all starting points before running BFS.
- **Level-by-Level Processing:** Snapshotting `len(q)` at the start of a loop allows tracking discrete time steps or levels.
- **In-Place State Tracking:** Mutating state values directly in the matrix (e.g., `1 -> 2`) prevents duplicate visits without extra auxiliary memory.

---

# Common Mistakes

## Mistake 1: Incrementing Time Per Node Instead of Per Level

Incrementing `time += 1` inside the `while q` loop for every single `popleft()` treats sequential node processing as distinct minutes, inflating the final time.

Fix:

- Process all nodes belonging to the current minute in a level loop (`for _ in range(len(q))`) before incrementing `time`.

---

## Mistake 2: Incrementing Time on the Final Empty Level

If the loop condition is only `while q`, `time` will increment one final time after all fresh oranges have rotted and the remaining elements in the queue are popped without rotting anything new.

Fix:

- Add `fresh_count > 0` to the loop guard: `while q and fresh_count > 0:`.

---

## Mistake 3: Forgetting Unreachable Fresh Oranges

Assuming that empty queue equals all oranges rotted. If a fresh orange is surrounded by empty cells (`0`), it can never be reached by rot.

Fix:

- Keep track of `fresh_count` and return `-1` if `fresh_count > 0` after the BFS terminates.

---

# Additional Resources

- [https://neetcode.io/problems/rotting-oranges](https://www.google.com/search?q=https://neetcode.io/problems/rotting-oranges)
- [https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)