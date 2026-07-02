---
title: Leetcode 1046 - Last Stone Weight
tags:
  - leetcode
  - neetcode-150-list
  - python
  - max-heap
updated_date: 2026-07-02
url: https://leetcode.com/problems/last-stone-weight/
---

# Leetcode 1046 - Last Stone Weight

## Understanding the Problem

The problem asks us to simulate a game where we repeatedly smash the two heaviest stones together until at most one stone is left.

Each turn, we choose the two heaviest stones, say $x$ and $y$ (with $x \ge y$):

- If $x == y$, both stones are totally destroyed.
- If $x \neq y$, the stone of weight $y$ is destroyed, and the stone of weight $x$ has a new weight of $x - y$.

---

## Solution Implementation

To efficiently pull the two heaviest elements repeatedly, a **Max-Heap** is the ideal data structure. Since Python's `heapq` library only implements a **Min-Heap** by default, we can simulate a Max-Heap by **inverting the signs** (negating) of all the stone weights:

- The largest positive weight becomes the smallest negative number, placing it at the top (root) of the min-heap.
- When popping, we negate the value again to restore its original positive weight.

### Code

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Invert weights to simulate a Max-Heap using Python's Min-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # Smash stones until 1 or 0 stones remain
        while len(stones) > 1:
            x = -heapq.heappop(stones) # Heaviest stone
            y = -heapq.heappop(stones) # Second heaviest stone

            if x != y:
                # Push the remaining weight back as a negative number
                heapq.heappush(stones, -(x - y))

        # If a stone remains, return its positive weight; otherwise, return 0
        return -stones[0] if stones else 0
```

### Time Complexity

- Heap Initialization - Transforming the array into a heap takes $O(N)$ time.
- Simulation Loop - In the worst-case scenario, we process $N-1$ smashes. Each smash involves two pops ($O(\log N)$ each) and potentially one push ($O(\log N)$). Therefore, the loop takes $O(N \log N)$ time.

**Overall time complexity - $O(N \log N)$**

### Space Complexity

- Heap Storage: We mutate the original list or create an inverted list of size $N$ to hold the heap elements.

**Overall space complexity - $O(N)$**

## Additional Resources

- https://neetcode.io/problems/last-stone-weight/
- https://leetcode.com/problems/last-stone-weight/
