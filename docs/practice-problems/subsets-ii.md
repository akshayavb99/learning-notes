---
title: Leetcode 90 - Subsets II
tags:
  - leetcode
  - neetcode-150-list
  - python
  - backtracking
  - recursion
updated_date: 2026-07-16
url: https://leetcode.com/problems/subsets-ii/
---

# Leetcode 90 - Subsets II

## Understanding the Problem

The goal is to return all possible subsets (the power set) of an integer array `nums` that may contain **duplicates**. The solution set must not contain duplicate subsets, and the subsets can be returned in any order.

To solve this efficiently using backtracking, we model the process as a decision tree where at each step, we decide whether to include an element or skip it. However, because the input array contains duplicate values, picking identical values at the same decision level would generate identical branches, leading to duplicate subsets.

- **Sorting for Duplicate Grouping:** By sorting `nums` initially, we ensure all duplicate elements are adjacent. This allows us to easily detect and skip identical choices.
- **State Tracking:** We use an index `idx` to track our current position in the array and a list `curr_list` representing the subset built along the current path.
- **Pruning Strategy:** When iterating through the available elements starting from `idx`, we allow the first occurrence of a number (`i == idx`). For subsequent iterations at the same depth level (`i > idx`), if `nums[i] == nums[i-1]`, we skip it. This ensures we don't start identical recursion branches with the same value.

---

## Solution Implementation

### Code

```python
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sort the array so that duplicate elements are adjacent
        nums.sort()

        def dfs(idx: int, curr_list: List[int]):
            # Every state reached in the state-space tree is a valid subset
            result.append(curr_list.copy())

            for i in range(idx, len(nums)):
                # Skip duplicate elements at the current recursion level
                if i > idx and nums[i] == nums[i-1]:
                    continue

                # Make the choice
                curr_list.append(nums[i])
                # Explore deeper choices (move to the next index)
                dfs(i + 1, curr_list)
                # Undo the choice (backtrack)
                curr_list.pop()

        dfs(0, [])
        return result
```

### Time Complexity

For an array of size $n$, a power set can have at most $2^n$ subsets. In the worst-case scenario where all elements are distinct, the algorithm explores all combinations. At each step, copying the `curr_list` into the `result` array takes $O(n)$ time. Sorting the initial array takes $O(n \log n)$ time.

**Overall time complexity — $O\left(n \cdot 2^n\right)$**

### Space Complexity

- **Recursion Stack:** The maximum depth of the recursion tree is equal to the number of elements in `nums`, giving a call stack depth of $O(n)$.
- **State Tracking:** The `curr_list` stores at most $n$ elements at any point during execution, taking $O(n)$ auxiliary space.

**Overall space complexity — $O(n)$** _(excluding the space required to store the final output)_

---

## Additional Resources

- https://neetcode.io/problems/subsets-ii
- https://leetcode.com/problems/subsets-ii/
