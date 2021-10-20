# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Closed_Islands

<h1>Number of Closed Islands</h1>

<p>
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
</p>
<p>
Return the number of closed islands.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png">

    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation: 
    Islands in gray are closed because they are completely surrounded by water (group of 1s).

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png">

    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1

<b>Example 3:</b>

    Input: grid = [[1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,1,0,1,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,0,0,0,0,1],
                   [1,1,1,1,1,1,1]]
    Output: 2
<b>Constraints:</b>

- 1 <= grid.length, grid[0].length <= 100
- 0 <= grid[i][j] <=1

<h2>Solution</h2>

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid),len(grid[0])
        def dfs(row, col, val):
            if 0<=row<rows and 0<=col<cols and grid[row][col]==0:
                grid[row][col] = val
                dfs(row+1,col, val)
                dfs(row-1,col, val)
                dfs(row,col+1, val)
                dfs(row,col-1, val)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j==0 or i==rows-1 or j==cols-1) and grid[i][j] == 0:
                    dfs(i,j,1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    res+=1
                    dfs(i,j,1)
        
        return res
```
