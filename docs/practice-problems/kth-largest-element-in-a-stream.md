---
title: Leetcode 703 - Kth Largest Element in a Stream
tags:
  - leetcode
  - neetcode-150-list
  - python
  - min-heap
updated_date: 2026-07-01
url: https://leetcode.com/problems/kth-largest-element-in-a-stream/
---

# Leetcode 703 - Kth Largest Element in a Stream

## Understanding the Problem

The goal is to design a class that finds the **$k$-th largest element** in a stream of integers. The stream is dynamic, meaning elements will be continuously added, and we need to return the $k$-th largest element after each insertion.

Instead of sorting the entire list every time an element is added (which is highly inefficient), we can use a **Min-Heap** of fixed size $k$:

- A Min-Heap keeps the smallest element at the top (root).
- If we maintain exactly $k$ elements in our Min-Heap, the smallest element in that heap will naturally be the $k$-th largest element of the entire stream.
- When a new element is added:
  1. Push it into the heap.
  2. If the heap size exceeds $k$, pop the smallest element.
  3. The root of the heap (`heap[0]`) is our answer.

---

## Solution Implementation

### Code

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only the k largest elements in the min-heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # If heap exceeds size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # The root of the min-heap is the k-th largest element
        return self.heap[0]
```

### Time Complexity

- Time to initialize the min heap - Heapifying the initial array takes $O(N)$ time. Popping the extra elements until the heap size reduces to $k$ takes $O((N - k) \log N)$ time. Thus, the initial setup takes $O(N \log K)$ if done via sequential insertion, or roughly $O(N)$ with a bulk heapify followed by trimming.
- Stream Addition - Inserting an element into a heap of size $k$ and potentially removing the minimum element takes $O(\log k)$ time.

**Overall time complexity - $O(\log k)$**

### Space Complexity

- Heap Storage: We only retain up to $k$ elements in our min-heap at any given time.

**Overall space complexity - $O(k)$**

## Additional Resources

- https://neetcode.io/problems/kth-largest-integer-in-a-stream/question
- https://leetcode.com/problems/kth-largest-element-in-a-stream/
