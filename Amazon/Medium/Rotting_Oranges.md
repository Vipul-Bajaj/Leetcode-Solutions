# [Home](./../..)/[Amazon](./..)/[Medium](./)/Rotting_Oranges
<h1>Rotting Oranges</h1>

<p>
You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png">

    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    
<b>Example 2:</b>

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    
<b>Example 3:</b>

    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

<h2>Solution</h2>

```python
class Solution:
    def get_val(self,grid,i,j,r,c):
        if i>=r or i<0 or j>=c or j<0:
            return 0
        return grid[i][j]
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        m,n = len(grid),len(grid[0])
        
        fresh_oranges=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh_oranges+=1
                    
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        q.append([-1,-1])
        
        t = -1
        
        while q:
            r,c = q.pop(0)
            if r == -1:
                t+=1
                if q:
                    q.append([-1,-1])
            else:
                for d in dirs:
                    new_r,new_c = r+d[0],c+d[1]
                    if self.get_val(grid,new_r,new_c,m,n) == 1:
                        grid[new_r][new_c] = 2
                        fresh_oranges-=1
                        q.append([new_r,new_c])
                        
        return t if fresh_oranges==0  else -1
```
