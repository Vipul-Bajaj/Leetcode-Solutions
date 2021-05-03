# [Home](./../..)/[Amazon](./..)/[Medium](./)/Unique_Paths_II
<h1>Unique Paths II</h1>

<p>
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg">

    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg">

    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1
    
<b>Constraints:</b>

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        # print(dp)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        # print(dp)
        return dp[m-1][n-1]
```
