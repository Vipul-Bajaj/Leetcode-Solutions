# [Home](./../../..)/[Google](./../..)/[Hard](./..)/Longest_Increasing_Path_in_a_Matrix
# [Home](./../../..)/[Google](./../..)/[Hard](./..)/Longest_Increasing_Path_in_a_Matrix
<h1>Longest Increasing Path in a Matrix</h1>

<p>
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg">

    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg">

    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
    
<b>Example 3:</b>

    Input: matrix = [[1]]
    Output: 1

<b>Constraints:</b>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def get_val(self,grid,i,j,r,c):
        if i>=r or i<0 or j>=c or j<0:
            return 0
        return grid[i][j]
    
    def dfs(self,grid,i,j,r,c,dp):
        if i>=r or i<0 or j>=c or j<0:
            return
        if dp[i][j]:
            return dp[i][j]
        
        dp[i][j] = 1
        temp = 0
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        
        for k in range(4):
            new_i = i + dirs[k][0]
            new_j = j + dirs[k][1]
            val = self.get_val(grid,new_i,new_j,r,c)
            if grid[i][j] < val:
                temp = max(temp,self.dfs(grid,new_i,new_j,r,c,dp))
       
        dp[i][j]+=temp 
        return dp[i][j]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        dp = [[0 for j in range(c)]for i in range(r)]
        
        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(ans,self.dfs(matrix, i,j,r,c,dp,))
        
        return ans
```
