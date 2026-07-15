---
title: Leetcode 973 - K Closest Points to Origin
tags:
  - leetcode
  - neetcode-150-list
  - python
  - max-heap
updated_date: 2026-07-03
url: https://leetcode.com/problems/k-closest-points-to-origin/
---

# Leetcode 973 - K Closest Points to Origin

## Understanding the Problem

The objective is to find the $k$ closest points to the origin $(0,0)$ on a 2D plane. The distance between a point $(x, y)$ and the origin is measured using the Euclidean distance formula:

$$\text{Distance} = \sqrt{x^2 + y^2}$$

> 💡 **Optimization Trick:** Because we only need to _compare_ relative distances rather than compute the true geometric value, we can omit the expensive square root operation ($\sqrt{}$) and simply compare the squared values ($x^2 + y^2$).

To track the closest points efficiently without sorting the entire array, we use a **Max-Heap** constrained to a fixed size $k$:

- Python's `heapq` module is a **Min-Heap** by default. We can invert this behavior by multiplying our distance values by $-1$.
- We iterate through the coordinates, pushing each point's negative distance along with its coordinates onto the heap.
- If the size of our heap exceeds $k$, we pop the top element. Because of the negative inversion, the top element represents the _largest_ absolute distance among our tracked choices, effectively purging the point farthest from the origin.
- After processing all points, the heap will contain exactly the $k$ closest points.

---

## Solution Implementation

### Code

```python
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []

        for x, y in points:
            # Calculate squared Euclidean distance to avoid float square roots
            dist = x**2 + y**2

            # Push negative distance to simulate a Max-Heap using heapq
            heapq.heappush(max_heap, (-dist, x, y))

            # If the heap exceeds size k, evict the point farthest from the origin
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract original coordinates from the remaining k elements
        return [[x, y] for (dist, x, y) in max_heap]
```

### Time Complexity

- **Heap Operations:** We iterate through all $N$ points in the input list. For each point, we push it onto a heap that holds at most $k + 1$ elements. Pushing and popping from a heap of size $k$ takes $O(\log k)$ time.
- **Extraction:** Building the final list from the remaining $k$ elements takes $O(k \log k)$ time.

**Overall time complexity — $O(N \log k)$**

### Space Complexity

- **Heap Storage:** The heap dynamically maintains up to $k + 1$ elements at any given stage of the loop.

**Overall space complexity — $O(k)$**

## Additional Resources

- https://neetcode.io/problems/k-closest-points-to-origin
- https://leetcode.com/problems/k-closest-points-to-origin/
