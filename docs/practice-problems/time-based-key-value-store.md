---
title: Leetcode 981 - Time Based Key-Value Store
tags:
  - leetcode
  - neetcode-150-list
  - python
  - binary-search
  - array
  - hashmap
updated_date: 2026-06-03
url: https://leetcode.com/problems/time-based-key-value-store/description/
---

# [Leetcode 981 - Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)

## Understanding the Problem

Key-value stores can be implemented with dictionaries (hashmaps) in Python. We know for every key there can be different values at different timestamps. So each value in the dictionary can be a list of pair of values - the timestamp and the actual value. Each pair is an element of the list and can be implemented as a list or tuple

Setting a key's value at a given timestamp is straightforward - Simply append the pair to the list at the required key.

To get the value at the largest timestamp lesser than equal to the required timestamp, the brute force approach could be to iterate over all the list elements for the given key, find the pair with largest timestamp lesser than or equal to desired timestamp, and return the value. However, this gives a suboptimal approach of $O(n)$ on average.

Since we know the timestamps arrive in increasing order and are in integer form, we can reduce the search time to $O(log n)$ by using binary search

## Solution Implementation

### Code

```python
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.tmap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

### Time Complexity

- Time to set key-value pair at a timestamp - **$O(1)$**
- Time to get value for a given key and an upper bound timestamp - **$O(log n)$**

### Space Complexity

- Space to store key-value pairs across timestamps - $O(m \times n)$, where $m$ is number of keys and $n$ is average number of timestamps per key

**Overall space complexity - $O(m \times n)$**

## Additional Resources

- https://neetcode.io/problems/time-based-key-value-store/question
