---
title: DSA Patterns Revision Sheet
description: >
  This page is a summary of important DSA patterns which I think will be useful when revising for interviews.
tags: [dsa, interview_preparation]
---

# DSA Patterns Revision Sheet

## Sliding Window

### What is the pattern about?

A technique that maintains a **window (subarray/substring)** over a sequence and moves it efficiently instead of recomputing results from scratch.
The window can expand, shrink, or slide based on conditions.

### Why is it used?

Imagine you are asked to find something like:

- the best subarray of size K
- the longest substring with a rule
- the minimum/maximum value in every continuous segment

A brute-force way would be:

- pick every possible subarray
- compute answer from scratch each time

  This becomes **O(n²) or worse**

Sliding window improves this by:

- keeping track of a **running result (sum, frequency, count, etc.)**
- when the window moves, you only:
  - **add the new element entering the window**
  - **remove the element leaving the window**

So instead of recalculating the entire window, you just **update the previous answer slightly**. This makes it:

- very fast (usually O(n))
- ideal for problems involving **continuous segments of data**

### Types / Variations

- Fixed-size window
- Variable-size window
- At most K / Exactly K constraints
- Minimum window (shrink to optimize)
- Sliding window with hashmap / frequency count

### Relevant Data Structures

- Arrays / Strings
- HashMap / Dictionary
- Set
- Counter (frequency array)

### When to use?

- Keywords:
  - “subarray” / “substring”
  - “longest / shortest”
  - “continuous / contiguous”
  - “at most / exactly K”

- Problems involving:
  - Window-based constraints
  - Counting or optimizing over ranges

### When NOT to use?

- Non-contiguous problems
- Problems requiring all combinations (use backtracking)
- When order doesn't matter (consider hashing instead)
- Tree/graph traversal problems

### Template (Pseudocode)

**Fixed Window (Window size is constant)**

```
window_sum = 0
for i in range(k):
    window_sum += arr[i]

max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    max_sum = max(max_sum, window_sum)
```

**Variable Window (Window size is not fixed and can change based on required conditions)**

```
left = 0
for right in range(n):
    include arr[right] into window

    while window is invalid:
        remove arr[left]
        left += 1

    update result
```

### Time & Space Complexity

- Time: **O(n)**
- Space: **O(1) or O(k)** if using hashmap

### Classic Problems / Triggers

- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Maximum Sum Subarray of Size K

### Common Mistakes / Pitfalls

- Forgetting to shrink window properly
- Incorrect validity condition
- Off-by-one errors
- Updating result at wrong time
- Using it on non-contiguous problems

### Edge Cases to Watch

- Empty input
- Window size > array size (Invalid window)
- All elements identical (Ensure the window is adjusted properly)
- Negative numbers
- K = 0 (Invalid window) or K = 1 (Every window is valid)

## Reference

1. https://thetorangi.github.io/DSA-cheat-sheet/
