---
title: Leetcode 78 - Subsets
tags:
  - leetcode
  - neetcode-150-list
  - python
  - backtracking
  - recursion
updated_date: 2026-07-07
url: https://leetcode.com/problems/subsets/
---

# Leetcode 78 - Subsets

## Understanding the Problem

The goal is to return the power set (all possible subsets) of a given array of unique integers, `nums`. A subset can be of any length, from the empty set `[]` to the entire array itself, and the elements in the subsets must not contain duplicates.

To solve this, we can model the decision-making process as a **Backtracking (DFS)** tree. For every element in the array, we have two fundamental choices:
1. **Include** the current element in our subset.
2. **Exclude** the current element from our subset.

By systematically making these choices for each element from left to right, we naturally explore every single unique combination.



- **State Tracking:** We use an index `i` to keep track of our position in `nums` and a dynamic list `curr_set` to hold the subset we are building.
- **Base Case:** When our index `i` equals the length of `nums`, it means we have made a choice for every element. At this point, a copy of `curr_set` is appended to our final results.
- **Backtracking Mechanism:** After exploring the recursive branch that includes an element (`curr_set.append(nums[i])`), we must clean up our state by removing that same element (`curr_set.pop()`) before exploring the branch that *excludes* it. This ensures that subsequent branches aren't polluted by previous choices.

---

## Solution Implementation

### Code

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, curr_set):
            # Every state reached is a valid subset, append it immediately
            result.append(list(curr_set))
            
            # Explore all possible next elements
            for j in range(i, len(nums)):
                curr_set.append(nums[j])
                dfs(j + 1, curr_set)  # Move forward to avoid duplicates
                curr_set.pop()         # Backtrack
        
        dfs(0, [])
        return result
```

### Time Complexity

At each step of the array of size $n$, the algorithm branches out to explore combinations. The loop-based backtracking approach visits exactly $2^n$ unique states, each corresponding to a unique subset in the power set. When entering each recursive call, copying the `curr_set` into our results array takes $O(n)$ time in the worst case.

**Overall time complexity — $O\left(n \cdot 2^n\right)$**

### Space Complexity

- **Recursion Stack:** The maximum depth of our recursion tree is exactly $n$, corresponding to the scenario where all elements are included in the subset. Thus, the call stack uses $O(n)$ space.
- **State Tracking:** The `curr_set` list grows to a maximum size of $n$ elements during execution. Excluding the memory required to hold the final output list, the auxiliary space is dominated by the depth of this recursion tree.

**Overall space complexity — $O(n)$**

---

## Additional Resources

- https://neetcode.io/problems/subsets
- https://leetcode.com/problems/subsets/