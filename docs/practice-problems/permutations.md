---
title: Leetcode 46 - Permutations
tags:
  - leetcode
  - neetcode-150-list
  - python
  - backtracking
  - recursion
updated_date: 2026-07-14
url: https://leetcode.com/problems/permutations/
---

# Leetcode 46 - Permutations

## Understanding the Problem

The goal is to return all possible permutations of an array of distinct integers, `nums`. A permutation is an arrangement of all the elements from the input array in a specific order. Since the elements are unique, an array of length $n$ will always yield exactly $n!$ unique permutations.

To solve this, we can model the process by **inserting elements one by one** into an existing list. For each new number from `nums`, we explore every possible position (index) where it can be inserted into our current permutation build path.

- **State Tracking:** We use an index `idx` to track which element from `nums` we are currently placing, and a list `curr_list` representing the permutation built so far.
- **Base Cases:** 1. If the length of `curr_list` matches the length of `nums`, we have successfully placed every element. A copy of `curr_list` is added to the results. 2. If `idx` goes out of bounds, we terminate the branch.
- **Placement Mechanism:** In the loop, `i` ranges from `0` to `len(curr_list)`. This represents all the possible slots (before, between, or after existing elements) where `nums[idx]` can be inserted. Slicing `curr_list[:i] + [nums[idx]] + curr_list[i:]` generates a new list state for the next recursive step without mutating the original list, naturally eliminating the need for an explicit manual pop/backtrack step.

---

## Solution Implementation

### Code

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(idx, curr_list):
            # Base case: a complete permutation is formed
            if len(curr_list) == len(nums):
                result.append(curr_list.copy())
                return

            if idx >= len(nums):
                return

            # Insert the current number at every possible position in the current list
            for i in range(0, len(curr_list) + 1):
                dfs(idx + 1, curr_list[:i] + [nums[idx]] + curr_list[i:])

        dfs(0, [])
        return result
```

### Time Complexity

The algorithm generates all possible permutations of the input array. For an array of size $n$, there are exactly $n!$ unique permutations. At each step of the recursion tree, creating a new list state via slicing and list concatenation takes $O(n)$ time. Additionally, copying the final valid list into the results array takes $O(n)$ time.

**Overall time complexity — $O\left(n \cdot n!\right)$**

### Space Complexity

- **Recursion Stack:** The maximum depth of the recursion tree corresponds to the number of elements in `nums`, which requires $O(n)$ stack space.
- **State Tracking:** In each recursive call, new lists are created via slicing. At any single moment along a call path, the maximum memory allocated for these lists is proportional to the depth of the tree, which takes $O(n)$ space.

**Overall space complexity — $O(n)$**

---

## Additional Resources

- https://neetcode.io/problems/permutations
- https://leetcode.com/problems/permutations/
