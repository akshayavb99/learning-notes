---
title: Leetcode 110 - Balanced Binary Tree
tags:
  - leetcode
  - neetcode-150-list
  - python
  - tree
  - dfs
updated_date: 2026-06-15
url: https://leetcode.com/problems/balanced-binary-tree/description/
---

# [Leetcode 543 - Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

## Understanding the Problem

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by less than or equal to 1.

## Solution Implementation

At each node, we can find the left and right subtree heights. If the variation in heights is more than 1, we can update the overall result to `False`.

We can use the concept of member variables and nested helper functions in the case of Python

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True

        def isBalancedHelper(node):
            nonlocal res
            if node is None:
                return 0

            left_height = isBalancedHelper(node.left)
            right_height = isBalancedHelper(node.right)

            if abs(left_height-right_height)>1:
                res = False
            else:
                res = res and True

            return 1 + max(left_height, right_height)

        isBalancedHelper(root)
        return res
```

### Time Complexity

- Time to iterate over all nodes - $O(n)$

Overall time complexity is $O(n)$.

### Space Complexity

- Space to recursively iterate over the nodes - $O(h)$, where $h$ is the height of the tree. In a balanced tree, $h = O(log n)$ and imbalanced tree, $h = n$

Overall space complexity is $O(1)$.

## Additional Resources

- https://neetcode.io/problems/balanced-binary-tree/question
