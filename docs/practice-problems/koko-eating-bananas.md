---
title: Leetcode 875 - Koko Eating Bananas
tags:
    - leetcode
    - neetcode-150-list
    - python
    - binary-search
    - array
updated_date: 2026-06-02
url: https://leetcode.com/problems/koko-eating-bananas/description/
---

# [Leetcode 875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

## Understanding the Problem

Given a list where each element is a pile of some number of bananas and a required time target in hours, we need to find the minimum number of bananas to eat in one hour within the time target. An important point to note is that if a pile contains lesser number of bananas than the consumed number of bananas per hour, then the pile must be finished in that hour and the next pile is started from next hour.

The smallest number of bananas that can be in eaten in 1 hour is 1, and the maximum number of bananas is the number of bananas in the biggest pile. We can estimate that the more number of bananas consumed in one hour, the lesser the total time taken to eat all the piles.

A brute force approach would be to iterate from 1 banana per hour to maximum number of bananas across all piles, and choose the smallest number such that all piles are eaten within the desired number of hours. This search would take $O(n)$ time. However, the range of search `[1,2..., max-num]` is an ordered range, hence we can use binary search to look for the number of bananas to be eaten in one hour.


## Solution Implementation

In the binary search let's consider `left` and `right` as the two boundaries of the search at any given iteration. 

- We calculate the number of bananas eaten per hour as `k=left + (right-left)//2`. 
- If the time taken to eat all banana piles is greater than the target time, then we need to increase the number of bananas eaten per hour = Move left boundary to `k+1`.
- If the time taken to eat all banana piles is lesser than the target time, then we need to decrease the number of bananas eaten per hour to find the minimum possible number = Move right boundary to `k`.

### Code

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingSpeed(k):
            # Helper function to calculate the time taken to eat all piles for given k (number of bananas per hour)
            return sum([-(-p//k) for p in piles])
        
        left = 1
        right = max(piles)
        min_k = float("inf")
        while left < right:
            k = left + (right-left)//2
            if eatingSpeed(k) > h:
                left = k+1
            else:
                right = k
        min_k = min(min_k, right)

        return min_k

```

### Time Complexity

- Time to find maximum number of bananas eaten per hour (right boundary initialization) - $O(n)$ where $n$ is length of the input array -> a
- Time for each binary search iteration - $O(log(m))$ where $m$ is the maximum number of bananas in a pile -> b
- Time for total time to eat all piles given per hour bananas count - $O(n)$ -> c

**Overall time complexity - $O((c \times b) + a) = O(n \times log(m))$**


### Space Complexity

Space required for binary search and other variables = $O(1)$

**Overall space complexity - $O(1)$**


## Additional Resources

- https://neetcode.io/problems/eating-bananas/question
