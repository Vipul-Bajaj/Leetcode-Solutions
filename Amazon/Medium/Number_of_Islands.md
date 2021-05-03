# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Number_of_Islands
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Number_of_Islands
<h1>Number of Islands</h1>

<p>
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

</p>

<b>Example 1:</b>

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

<b>Example 2:</b>

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

<h2>Solution</h2>

```python
class Solution:
    def get_val(self,grid,i,j,r,c):
        if i>=r or i<0 or j>=c or j<0:
            return 0
        return grid[i][j]
    
    def dfs(self,grid,i,j,r,c,visited):
        if i>=r or i<0 or j>=c or j<0:
            return
        visited[i][j] = True
        
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        
        for k in range(4):
            new_i = i + dirs[k][0]
            new_j = j + dirs[k][1]
            val = self.get_val(grid,new_i,new_j,r,c)
            if val == "1" and not visited[new_i][new_j]:
                self.dfs(grid,new_i,new_j,r,c,visited)

            
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid),len(grid[0])
        visited = [[False for j in range(c)]for i in range(r)]
        
        islands = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and not visited[i][j]:
                    islands+=1
                    self.dfs(grid, i,j,r,c,visited)
        
        return islands
```
