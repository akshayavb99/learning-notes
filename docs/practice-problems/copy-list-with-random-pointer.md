---
title: Leetcode 138 - Copy List with Random Pointer
tags:
  - leetcode
  - neetcode-150-list
  - python
  - linked-list
  - hashmap
updated_date: 2026-06-08
url: https://leetcode.com/problems/copy-list-with-random-pointer/description/
---

# [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

## Understanding the Problem

First step is to understand what a 'deep copy' means. Deep copy means that the copy is an exact replica of the original, but occupies distinct memory separate from the original. In the case of linked lists, it means that there are 2 linked lists with exactly same values, but the nodes themselves are separate, even if they replicate the relationship of the original linked list.

## Solution Implementation

When creating the deep copy, we need a way to keep track of the old nodes and the new nodes as respective pairs. This can be done using hashmaps where the old nodes are the keys and new nodes are the values.

We can have a two-pass solution where:

1. Pass 1 - Create all the new nodes and map the old node-new node pairs in hashmap
2. Pass 2 - Iterate over each node (followed by its next node), and use the hashmap to find the new nodes corresponding to the old node's `next` and `random`connections.

### Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        list_copy = {None:None}
        node = head
        while node:
            new_node = Node(node.val, None, None)
            list_copy[node] = new_node
            node = node.next

        node = head
        while node:
            new_node = list_copy[node]
            new_node.next = list_copy[node.next]
            new_node.random = list_copy[node.random]
            node = node.next

        return list_copy[head]

```

### Time Complexity

- Time to build deep copies of the nodes - $O(n)$
- Time to build the `next` and `random` connections between the copy nodes - $O(n)$

**Overall time complexity - $O(n)$**

### Space Complexity

- Space to store the hashmap - $O(2n)$

**Overall space complexity - $O(n)$**

## Additional Resources

- https://neetcode.io/problems/copy-linked-list-with-random-pointer/question
