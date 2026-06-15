---
title: Leetcode 146 - LRU Cache
tags:
  - leetcode
  - neetcode-150-list
  - python
  - linked-list
  - hashmap
updated_date: 2026-06-15
url: https://leetcode.com/problems/lru-cache/description/
---

# [Leetcode 146 - LRU Cache](https://leetcode.com/problems/lru-cache/description/)

## Understanding the Problem

The requirement is to write a Least Recently Used class, with the following functionalities:

1. Initialize cache with positive capacity
2. For a given key, return the value if the key exists else -1
3. For a given key-value pair, insert (if key does not exist) or update (if key exists) the key-value in the cache. If the cache capacity is exceeded, remove the least recently used key-value pair

Both the `get` and `put` functionalities need to have $O(1)$ time complexity.

## Solution Implementation

The implementation asks to store key-value pairs, hence hashmap (Python dictionaries) is the choice of data structure.

There is a need to track the order in which the keys were accessed (either `get` or `put`), while ensuring the reordering due to key-value access also takes $O(1)$ time. For this, we need to be able to access each key-value pair at $O(1)$ time (taken care of by the hashmap), and reorder them in $O(1)$ time. This can be done with the help of doubly linked list, and hence we will define an extra class `Node` to store the key-value pairs as nodes of a linked list

### Code

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map the key to nodes
        self.left, self.right = Node(), Node() # Left is least recent, right is most recent
        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from anywhere in list
    def remove(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    # Insert as most recent
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove self.key from linked list - put it at the right most position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

```

### Time Complexity

- Time to get a value - $O(1)$
- Time to put a value - $O(1)$

Overall time complexity is $O(1)$.

### Space Complexity

- Space to store hashmap - $O(n)$
- Space to store linked list - $O(n)$

Overall space complexity is $O(1)$.

## Additional Resources

- https://neetcode.io/problems/lru-cache/question
