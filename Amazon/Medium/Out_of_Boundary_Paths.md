# [Home](./../..)/[Amazon](./..)/[Medium](./)/Out_of_Boundary_Paths
<h1>Out of Boundary Paths</h1>

<p>
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
</p>
<p>
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png">

    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png">

    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12

<b>Constraints:</b>

- 1 <= m, n <= 50
- 0 <= maxMove <= 50
- 0 <= startRow <= m
- 0 <= startColumn <= n

<h2>Solution</h2>

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        
        dp = [[0 for j in range(n)]for i in range(m)]
        
        dp[startRow][startColumn] = 1
        count = 0
        for k in range(1,maxMove+1):
            temp = [[0 for j in range(n)]for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        count = (count + dp[i][j])%mod
                    if j == n-1:
                        count = (count + dp[i][j])%mod    
                    if i == 0:
                        count = (count + dp[i][j])%mod
                    if j == 0:
                        count = (count + dp[i][j])%mod
                    temp[i][j] = ((dp[i-1][j] if i>0 else 0 )+ (dp[i+1][j] if i<m-1 else 0))%mod + ((dp[i][j-1] if j>0 else 0) + (dp[i][j+1] if j<n-1 else 0))%mod 
            dp = temp.copy()
        return count
```
