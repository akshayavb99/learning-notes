---
title: Leetcode 543 - Diameter of Binary Tree
tags:
  - leetcode
  - neetcode-150-list
  - python
  - tree
  - dfs
updated_date: 2026-06-15
url: https://leetcode.com/problems/diameter-of-binary-tree/description/
---

# [Leetcode 543 - Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)

## Understanding the Problem

The requirement is to calculate the diameter of a binary tree, which is the largest distance between any 2 nodes. Note that, this diameter can be calculated without passing through the root node if necessary.

## Solution Implementation

At each node, we can calculate the largest diameter seen till the node, by using the left subtree height and right subtree height.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def diameterHelper(node):
            nonlocal max_diameter
            if node is None:
                return 0

            left_height = diameterHelper(node.left)
            right_height = diameterHelper(node.right)

            max_diameter = max(max_diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        diameterHelper(root)
        return max_diameter
```

### Time Complexity

- Time to calculate the diameter - $O(n)$

Overall time complexity is $O(n)$.

### Space Complexity

- Space for the DFS function call stack - $O(h)$, where $h$ is the height of the tree. In a balanced tree, $h = O(log n)$ and imbalanced tree, $h = n$

Overall space complexity is $O(1)$.

## Additional Resources

- https://neetcode.io/problems/binary-tree-diameter/question
