# [Home](./../..)/[Twiiter](./..)/[Medium](./)/Count_Sub_Islands
<h1>Count Sub Islands</h1>

<p>
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
</p>
<p>
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
</p>
<p>
Return the number of islands in grid2 that are considered sub-islands.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/06/10/test1.png">

    Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    Output: 3
    Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png">

    Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    Output: 2 
    Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

<b>Constraints:</b>

- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j] and grid2[i][j] are either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def dfs(self,grid1,grid2,rows,cols,row,col,visited,ok):
        ok[0]&=grid1[row][col]
        visited[row][col] = True
        for nr,nc in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
            if 0<=nr<rows and 0<=nc<cols and grid2[nr][nc] == 1 and not visited[nr][nc]:
                self.dfs(grid1,grid2,rows,cols,nr,nc,visited,ok)
        return
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
        visited = [[False for j in range(n)]for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    ok = [1]
                    self.dfs(grid1,grid2,m,n,i,j,visited,ok)
                    count+=ok[0]
        return count
```
