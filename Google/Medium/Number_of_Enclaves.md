# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Enclaves
<h1>Number of Enclaves</h1>

<p>
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
</p>
<p>
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
</p>
<p>
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg">

    Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 3
    Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg">

    Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    Output: 0
    Explanation: All 1s are either on the boundary or can reach the boundary.
    
<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid[i][j] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                list(map(dfs, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                
        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if i in (0, m-1) or j in (0, n-1):
                dfs(i, j)
                
        return sum(map(sum, grid))
```
