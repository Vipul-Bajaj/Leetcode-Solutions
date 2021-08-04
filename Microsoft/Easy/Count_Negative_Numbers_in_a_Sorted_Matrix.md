# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Count_Negative_Numbers_in_a_Sorted_Matrix
<h1>Count Negative Numbers in a Sorted Matrix</h1>

<p>
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
</p>

<b>Example 1:</b>

    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

<b>Example 2:</b>

    Input: grid = [[3,2],[1,0]]
    Output: 0

<b>Example 3:</b>

    Input: grid = [[1,-1],[-1,-1]]
    Output: 3

<b>Example 4:</b>

    Input: grid = [[-1]]
    Output: 1
    
<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- -100 <= grid[i][j] <= 100

<h2>Solution</h2>

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0
        for row in grid:
            j = n-1
            while j>=0 and row[j]<0:
                j-=1
            count += (n-j-1)
        return count
```
