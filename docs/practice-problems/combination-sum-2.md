---
title: Leetcode 40 - Combination Sum II
tags:
  - leetcode
  - neetcode-150-list
  - python
  - backtracking
  - recursion
updated_date: 2026-07-14
url: https://leetcode.com/problems/combination-sum-ii/
---

# Leetcode 40 - Combination Sum II

## Understanding the Problem

The goal is to find all unique combinations in a collection of candidate numbers (`candidates`) where the candidate numbers sum up to a target number (`target`). Unlike Combination Sum I, each number in `candidates` may only be used **once** in the combination, and the input array may contain duplicate numbers. The solution set must not contain duplicate combinations.

To solve this, we can model the decision-making process using a **Backtracking (DFS)** tree over a sorted array. Sorting is crucial because it allows us to easily skip duplicate elements and prune unnecessary search paths.

- **State Tracking:** We use an index `idx` to track our current position in the array, a dynamic list `curr_list` to hold the combination we are building, and a `curr_sum` to monitor the running total.
- **Base Cases:** 1. If `curr_sum` equals `target`, a valid combination is found, so a copy of `curr_list` is appended to the final results. 2. If `curr_sum` exceeds `target`, we return immediately (pruning the branch).
- **Avoiding Duplicates:** Within the loop, if an element is the same as the previous element (`candidates[i] == candidates[i-1]`) and it is not the first element of the current recursive level (`i > idx`), we skip it. This ensures we don't start identical combination pathways.
- **Backtracking Mechanism:** We add the element to `curr_list`, recurse forward to the next index (`i + 1`), and then remove the element (`curr_list.pop()`) to clean up the state before the next iteration.

---

## Solution Implementation

### Code

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(idx, curr_list, curr_sum):
            if curr_sum == target:
                result.append(curr_list.copy())
                return

            if curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                # Skip duplicate elements at the same depth level
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                # Pruning: early exit if the current element exceeds the remaining target
                if curr_sum + candidates[i] > target:
                    break

                curr_list.append(candidates[i])
                # Move to i + 1 to ensure each element is used only once
                dfs(i + 1, curr_list, curr_sum + candidates[i])
                curr_list.pop()  # Backtrack

        dfs(0, [], 0)
        return result
```

### Time Complexity

Sorting the array takes $O(n \log n)$ time. In the worst-case scenario (e.g., all elements are $1$ and the target is $n$), the algorithm generates up to $2^n$ state combinations. For every valid combination, creating a copy of the list takes $O(k)$ time, where $k$ is the length of the combination (bounded by $n$).

**Overall time complexity — $O\left(k \cdot 2^n\right)$**

### Space Complexity

- **Recursion Stack:** The maximum depth of the recursion tree is bounded by $n$ when picking elements one by one. This requires $O(n)$ space.
- **State Tracking:** The `curr_list` used to keep track of the current combination requires a maximum of $O(n)$ auxiliary space.

**Overall space complexity — $O(n)$**

---

## Additional Resources

- https://neetcode.io/problems/combination-target-sum-ii
- https://leetcode.com/problems/combination-sum-ii/
