# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Unique_Paths
# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Unique_Paths
<h1>Unique Paths</h1>

<p>
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png">

</p>

<b>Example 1:</b>

    Input: m = 3, n = 7
    Output: 28
    
<b>Example 2:</b>

    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
    
<b>Example 3:</b>

    Input: m = 7, n = 3
    Output: 28

<b>Constraints:</b>

- 1 <= m, n <= 100
- It's guaranteed that the answer will be less than or equal to 2 * 109.

<h2>Solution</h2>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        dp[0][0] = 1
        # print(dp)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        # print(dp)
        return dp[m-1][n-1]
```
