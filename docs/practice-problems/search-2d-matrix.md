---
title: Leetcode 74 - Search a 2D Matrix
tags:
    - leetcode
    - binary-search
    - matrix
    - neetcode-150-list
    - python
updated_date: 2026-06-01
url: https://leetcode.com/problems/search-a-2d-matrix/description/
---

# [Leetcode 74 - Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

## Understanding the Problem

Given a 2D matrix where the elements are sorted across rows and the columns, the objective is to find if the target number exists in the matrix.

The brute force approach would be to iterate over every single element in the matrix and check if it is equal to the target. The time complexity of this approach will be $O(rows \times columns)$

But the sorted order of the elements gives the advantage of using binary search to search for the target. Additionally, we can use binary search twice - once to find the row and once to find the column to identify the possible position of the target in the matrix. Using this method, it is possible to achieve a better time complexity of $O(log(rows) + log(columns)) = O(log(rows \times columns))$


## Solution Implementation

We begin by first searching for the range of rows in which the target could be present, using binary search. 

- If the target is lesser than the first element of a row, then it can be present in the rows before it (lower row index). 
- If the target is greater than the last element of a row, then it can be present in the rows after it (higher row index).

If a range of rows is successfully identified, the binary search loop can be stopped, and the the desired row is calculated as `(top+bot)//2`.

```python
top, bot = 0, R-1
while top <= bot:
    row = (top+bot)//2
    if target > matrix[row][-1]:
        top = row + 1
    elif target < matrix[row][0]:
        bot = row - 1
    else:
        break
        
if top > bot: # The loop ended because no suitable row was found where the target < 1st element and target <= last element of the row 
    return False
```
> **Why is the desired row `(top+bot)//2` instead of simply `top`?**
> 
> After the loop finishes, top does not necessarily equal the row you found. When the loop exits via break, the condition that caused the break was evaluated on `row = (top + bot) // 2`. At that point, `top <= row <= bot`, but top and row are not necessarily the same
> 
> For example: 
>
> ```python
> top = 4
> bot = 7
> row = (4 + 7) // 2 = 5
> ``` 
> Suppose row 5 contains the target range and we break. After the loop:
> 
> ```python
> top = 4
> bot = 7
> row = 5
> ```
> If you used `row = top`, you would get row 4, which is wrong. The correct row is the midpoint that was tested when the break occurred, `row = (top + bot) // 2`

Once the row is identified, the next binary search is along the columns.

```python
left, right = 0, C-1
while left <= right:
    col = (left + right)//2
    if target > matrix[row][col]:
        left = col + 1
    elif target < matrix[row][col]:
        right = col - 1
    else:
        return True
```

If the target cannot be found (`left > right` at any iteration), we can return `False`

### Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        top, bot = 0, R-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if top > bot:
            return False

        left, right = 0, C-1
        while left <= right:
            col = (left + right)//2
            if target > matrix[row][col]:
                left = col + 1
            elif target < matrix[row][col]:
                right = col - 1
            else:
                return True
        
        return False
```

### Time Complexity

- Time to find the possible range of rows - $O(log(rows))$
- Time to find the possible column - $O(log(columns))$

Overall time complexity is $O(log(rows) + log(columns)) = O(log(rows \times columns))$.

### Space Complexity

The space occupied by variables for the while and storing the matrix dimensions together contribute $O(1)$ space.

Overall space complexity is $O(1)$.

## Additional Resources

- https://neetcode.io/problems/search-2d-matrix/question
