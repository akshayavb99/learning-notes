---
title: Leetcode 846 - Hand of Straights
tags:
    - leetcode
    - neetcode-150-list
    - python
    - hash-table
    - greedy
    - sorting
updated_date: 2026-08-24
url: https://leetcode.com/problems/hand-of-straights/
---

# Leetcode 846 - Hand of Straights

## Understanding the Problem

The goal is to determine if a given array of card values (`hand`) can be rearranged into groups of size `groupSize`, where each group consists of consecutive integers.

Return:

- `True` if it is possible to divide the cards into valid consecutive groups.
- `False` otherwise.

---

# Key Data Structures

## 1. Frequency Counter (`collections.Counter`)

Tracks the count of each card value in the hand. This allows us to quickly check if a required card is available and decrement its count when used.

## 2. Unique Values Set (`set`)

Keeps track of unique card values present in the hand, making it efficient to skip missing values when searching for the next starting card.

---

# Optimal Approach Intuition

A greedy approach works best here because the smallest available card in the hand **must** be the starting point of its own group. Since no smaller card exists to cover it, it cannot be part of a group that starts lower.

> Always find the smallest available card and greedily form a consecutive sequence of length `groupSize` starting from it.

---

# Why Greedy with Counter/Map?

If we try to sort the entire array and use every element sequentially without tracking frequency efficiently, we can run into redundant checks or miss overlapping groups. Using a hash map combined with tracking the minimum value allows us to clear out groups starting from the lowest boundary upwards cleanly.

---

# How the Optimal Approach Works

## Step 1: Check Divisibility

If the total number of cards (`len(hand)`) is not cleanly divisible by `groupSize`, return `False` immediately.

---

## Step 2: Track Frequencies and Minimums

- Build a frequency counter (`hand_counter`).
- Extract unique values into a set (`hand_values`) and identify the global minimum (`min_val`).

---

## Step 3: Iteratively Build Groups

While cards remain (`hand_counter` is not empty):

1. Advance `min_val` until it points to a valid existing card in `hand_values`.
2. For the current `min_val`, attempt to form a consecutive group of size `groupSize` (i.e., `min_val + i` for `i` in range `0` to `groupSize - 1`).
3. If any required card is missing, return `False`. Otherwise, decrement its frequency. If a card's count drops to `0`, remove it from `hand_counter` and `hand_values`.

---

# Solution Implementation

```python
from collections import Counter
from typing import List


class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_counter = Counter(hand)
        hand_values = set(hand)

        min_val = min(hand_values)

        while hand_counter:
            while min_val not in hand_values:
                min_val += 1

            for i in range(groupSize):
                if min_val + i not in hand_values:
                    return False
                else:
                    hand_counter[min_val + i] -= 1
                    if hand_counter[min_val + i] == 0:
                        del hand_counter[min_val + i]
                        hand_values.remove(min_val + i)

        return True

```

---

# Complexity Analysis

Let:

- $N$ = total number of cards in `hand`
- $K$ = number of unique card values

## Time Complexity: $O(N + K \log K)$ or $O(N \text{ log } N)$ depending on implementation details

- Counting elements and setting up structures takes $O(N)$ time.
- In the worst case, each unique card value is processed, and finding/deleting elements takes proportional time relative to the value range or unique elements. Using sorting alternatives typically bounds it to $O(N \log N)$.

---

## Space Complexity: $O(N)$

- The hash map (`Counter`) and unique set store up to $N$ elements in the worst case where all elements are unique.

---

# Key Takeaways

- **Greedy Min-Start Strategy:** The smallest available element must initiate a group.
- **Divisibility Check:** Always weed out invalid sizes upfront.
- **Dynamic Cleanup:** Removing exhausted elements from tracking sets optimizes subsequent lookups.

---

# Common Mistakes

## Mistake 1: Forgetting to Check Divisibility

Proceeding with grouping logic when `len(hand) % groupSize != 0` wastes execution time and leads to out-of-bounds or incomplete group errors.

## Mistake 2: Failing to Clean Up Exhausted Keys

Leaving counts at zero inside lookup structures can cause infinite loops or incorrect missing-card assessments during minimum updates.

---

# Additional Resources

- [NeetCode - Hand of Straights](https://neetcode.io/solutions/hand-of-straights)
- [LeetCode 846 - Hand of Straights](https://leetcode.com/problems/hand-of-straights/)