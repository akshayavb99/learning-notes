---
title: Leetcode 2 - Add Two Numbers
tags:
  - leetcode
  - neetcode-150-list
  - python
  - linked-list
updated_date: 2026-06-10
url: https://leetcode.com/problems/add-two-numbers/description/
---

# [Leetcode 2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## Understanding the Problem

We are given two linked lists with the following properties:

1. Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order.
2. Each node contains exactly one digit ($0 - 9$).
3. The numbers do not contain any leading zeros, except the number $0$ itself.
4. Must return the sum as a new linked list, also formatted in reverse order.

When adding two numbers we typically align them by their rightmost digits, and add by moving from right to left. We can apply a similar method here, where we add the digits starting at the head, and keep track of any carry overs for the next digit. The result of the pair of digits summation is used as the value for the new result node.

Some edge cases to think about:

1. One number might have more digits than the other
2. The very last addition might generate a carry, even if both linked lists have been fully traversed for calculation
3. If both linked lists are `[0]`, then result should also be `[0]`

## Solution Implementation

### Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        # Keep going if either list has elements OR if there is a remaining carry
        while l1 or l2 or carry:
            # Get the values, defaulting to 0 if the list has already ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the total sum for this position
            total = val1 + val2 + carry

            # Correctly split total into new carry and the node's value
            carry = total // 10
            new_val = total % 10

            # Create the new node and advance our result list pointer
            current.next = ListNode(new_val)
            current = current.next

            # Advance l1 and l2 pointers safely
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

### Time Complexity

- Time to iterate over each node in both linked lists - **$O(m + n)$**, where $m$ and $n$ are lengths of the 2 linked lists

**Overall time complexity - $O(m + n)$**

### Space Complexity

- Space to store result linked list - $O(max(m,n))$

**Overall space complexity - $O(m + n)$**

## Additional Resources

- https://neetcode.io/problems/add-two-numbers/question
