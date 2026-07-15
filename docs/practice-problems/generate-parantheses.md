---
title: Leetcode 22 - Generate Parentheses
tags:
  - leetcode
  - neetcode-150-list
  - python
  - backtracking
  - recursion
  -
updated_date: 2026-07-04
url: https://leetcode.com/problems/generate-parentheses/
---

# Leetcode 22 - Generate Parentheses

## Understanding the Problem

The goal is to generate all combinations of well-formed parentheses given $n$ pairs. A combination is well-formed if every opening parenthesis `(` has a matching closing parenthesis `)` and no closing parenthesis appears without a preceding unmatched opening parenthesis.

To solve this efficiently, we use a **Backtracking (DFS)** approach to build the combinations incrementally branch by branch:

- We keep track of the remaining count of open brackets (`open_count`) and closing brackets (`close_count`) available to place.
- **Placing `(`:** We can always place an opening parenthesis as long as we have pairs left to open (`open_count > 0`).
- **Placing `)`:** We can only place a closing parenthesis if it doesn't violate well-formedness. This means we must have _more_ closing brackets remaining than opening brackets (`close_count > open_count`), proving that an open bracket is currently waiting to be matched.
- **Base Case:** When both `open_count` and `close_count` reach `0`, a valid combination of length $2n$ is complete and added to our results.

> 💡 **Avoid Mutating State Variables:** A common pitfall in Python backtracking is using `list.append()` inside recursive arguments (e.g., `curr_str.append('(')`). Because `append()` mutates lists in-place and returns `None`, it breaks the recursive chain. Utilizing immutable string concatenation (`curr_str + '('`) cleanly isolates state choices to their respective recursion paths.

---

## Solution Implementation

### Code

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(open_count, close_count, curr_str):
            # Base case: if no brackets are left to place, combination is valid
            if open_count == 0 and close_count == 0:
                result.append(curr_str)
                return

            # If we have open brackets left, we can always add one
            if open_count > 0:
                dfs(open_count - 1, close_count, curr_str + '(')

            # We can only add a close bracket if it matches a previously placed open one
            if close_count > open_count:
                dfs(open_count, close_count - 1, curr_str + ')')

        # Start the recursion tree with 'n' open and 'n' close brackets available
        dfs(n, n, "")
        return result

### Time Complexity

The number of valid parenthesis combinations generated is exactly equal to the $n$-th Catalan number:

$$C_n = \frac{1}{n+1}\binom{2n}{n}$$

The asymptotic growth of the Catalan number is bounded by $\frac{4^n}{n\sqrt{n}}$. Since we spend $O(n)$ time to construct and copy each valid string of length $2n$ into our final results array:

**Overall time complexity — $O\left(\frac{4^n}{\sqrt{n}}\right)$**

### Space Complexity

- **Recursion Stack:** The maximum depth of the runtime call stack corresponds to the maximum length of a combination string, which is $2n$ recursive frames.
- **State Tracking:** Each recursive frame stores a string configuration of at most length $2n$. Excluding the memory required to hold the final output list, the space is dominated by the depth of this recursion tree.

**Overall space complexity — $O(n)$**

---

## Additional Resources

- https://neetcode.io/problems/generate-parentheses
- https://leetcode.com/problems/generate-parentheses/
```
