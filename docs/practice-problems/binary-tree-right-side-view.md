---
title: Leetcode 199- Binary Tree Right Side View
tags:
  - leetcode
  - neetcode-150-list
  - python
  - binary-tree
  - bfs
  - deque
updated_date: 2026-06-30
url: https://leetcode.com/problems/binary-tree-right-side-view/description/
---

# Leetcode 199- Binary Tree Right Side View

## Understanding the Problem

Imagine you are standing on the right side of a binary tree. You want to return the values of the nodes you can see, ordered from top to bottom.

Essentially, this means you need to grab the last node of every level (the rightmost node) in the tree.

## Solution Implementation

We can solve this problem efficiently using a Breadth-First Search (BFS) / Level-Order Traversal approach. By utilizing a queue (deque), we can process the tree level by level.

For each level:

- Track the number of nodes currently in the queue (qLen).
- Loop through all nodes of that specific level.
- Keep updating a tracking variable (rightSide) with the current node. Since we loop from left to right, the last node processed in the loop will naturally be the rightmost node of that level.
- Append the children of each node (left first, then right) to the queue for the next level.
- After completing a level, if a valid rightmost node was found, append its value to our result list.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
```

### Time Complexity

- Time to iterate over all nodes - $O(n)$

Overall time complexity is $O(n)$.

### Space Complexity

- Space to recursively iterate over the nodes - $O(h)$, where $h$ is the height of the tree. In a balanced tree, $h = O(log n)$ and imbalanced tree, $h = n$

Overall space complexity is $O(h)$.

## Additional Resources

- https://neetcode.io/problems/binary-tree-right-side-view/question
- https://leetcode.com/problems/binary-tree-right-side-view/description/
