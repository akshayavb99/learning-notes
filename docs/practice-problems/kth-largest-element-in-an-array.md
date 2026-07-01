---
title: Leetcode 215 - Kth Largest Element in an Array
tags:
  - leetcode
  - neetcode-150-list
  - python
  - min-heap
updated_date: 2026-07-01
url: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
---

# Leetcode 215 - Kth Largest Element in an Array

## Understanding the Problem

The objective is to find the **$k$-th largest element** in an unsorted array. Note that it is the $k$-th largest element in sorted order, not the $k$-th distinct element.

We can solve this efficiently using a **Min-Heap** of size $k$:

1. We can build a min-heap from the first $k$ elements of the array.
2. For the remaining elements, if an element is larger than the root of the min-heap (the current $k$-th largest), we pop the root and push the new element.
3. Once we process the entire array, the root of our min-heap will hold the $k$-th largest element.

> **Optimization Tip:** Instead of pushing all elements into the heap and then popping down to size $k$ (which takes $O(N)$ space and $O(N \log N)$ time in the worst case), building a heap of size $k$ dynamically keeps our auxiliary space usage strict to $O(k)$.

---

## Solution Implementation

### Code

```python
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Initialize a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate through the rest of the elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
```

### Time Complexity

- Heapification: Creating a heap out of the first $k$ elements takes $O(k)$ time using the bottom-up heapify approach.Processing
- Remaining Elements: There are $N - k$ elements left. For each element, a push-pop operation on a heap of size $k$ takes $O(\log k)$ time.

**Overall time complexity - $O(k + (N - k) \log k)$**, which simplifies to $O(N \log k)$ in the worst case. This is significantly faster than sorting the entire array ($O(N \log N)$) when $k \ll N$.

### Space Complexity

- We only ever maintain a heap of size $k$.

**Overall space complexity - $O(k)$**

## Additional Resources

- https://neetcode.io/problems/kth-largest-integer-in-a-stream/question
- https://leetcode.com/problems/kth-largest-element-in-a-stream/
