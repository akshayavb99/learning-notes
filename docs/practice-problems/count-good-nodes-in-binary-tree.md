---
title: Leetcode 1448 - Count Good Nodes in Binary Tree
tags:
  - leetcode
  - neetcode-150-list
  - python
  - binary-tree
  - dfs
updated_date: 2026-06-30
url: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
---

# Leetcode 1448 - Count Good Nodes in Binary Tree

## Understanding the Problem

Given the `root` of a binary tree, a node $X$ in the tree is named **good** if in the path from root to $X$, there are no nodes with a value _greater_ than $X$.

This means a node is considered "good" if its value is **greater than or equal to** the maximum value encountered so far along the path from the root to that node.

## Solution Implementation

We can solve this problem using a Depth-First Search (DFS) traversal.

As we traverse from the root down to the leaf nodes, we pass along the maximum value seen so far on that specific path (`max_val`).

1. If the current node's value is greater than or equal to `max_val`, it is a good node. We count it as `1`, then update `max_val` to be this node's value.
2. If the current node's value is smaller than `max_val`, it is not a good node. We count it as `0`, and keep the current `max_val` unchanged.
3. We recursively repeat this for both the left and right subtrees and return the total sum of good nodes.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0

            # A node is good if its value is >= the maximum value seen so far
            current_good = 1 if node.val >= max_val else 0

            # Track the maximum value for the next deeper level
            max_val = max(max_val, node.val)

            # Combine current result with results from left and right subtrees
            return current_good + dfs(node.left, max_val) + dfs(node.right, max_val)

        # Start the traversal with the root value as the initial maximum
        return dfs(root, root.val) if root else 0
```

### Time Complexity

- Time to iterate over all nodes - $O(n)$

Overall time complexity is $O(n)$.

### Space Complexity

- Space to recursively iterate over the nodes - $O(h)$, where $h$ is the height of the tree. In a balanced tree, $h = O(\log n)$ and in an imbalanced tree, $h = n$.

Overall space complexity is $O(h)$.

## Additional Resources

- https://neetcode.io/problems/count-good-nodes-in-binary-tree
- https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
