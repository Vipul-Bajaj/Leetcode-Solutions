# [Home](./../..)/[Google](./..)/[Medium](./)/Minimum_Path_Sum
<h1>Minimum Path Sum</h1>

<p>
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
<br>
Note: You can only move either down or right at any point in time.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg">

    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
  
<b>Example 2:</b>

    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12
 
<b>Constraints:</b>

* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 200
* 0 <= grid[i][j] <= 100

<h2>Solution</h2>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    val = grid[i][j]
                elif i == 0:
                    val = grid[i][j]+grid[i][j-1]
                elif j == 0:
                    val = grid[i][j]+grid[i-1][j]
                else:
                    val = grid[i][j]+min(grid[i-1][j],grid[i][j-1])
                grid[i][j] = val
        return grid[m-1][n-1]
```
