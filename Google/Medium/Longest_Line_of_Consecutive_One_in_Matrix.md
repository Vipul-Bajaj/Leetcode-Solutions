# [Home](./../..)/[Google](./..)/[Medium](./)/Longest_Line_of_Consecutive_One_in_Matrix
<h1>Longest Line of Consecutive One in Matrix</h1>

<p>
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
</p>
<p>
The line could be horizontal, vertical, diagonal, or anti-diagonal.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/long1-grid.jpg">

    Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
    Output: 3
    
<b>Example 2:</b>    

<img src="https://assets.leetcode.com/uploads/2021/04/24/long2-grid.jpg">

    Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
    Output: 4

<b>Constraints:</b>

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 104
- 1 <= m * n <= 104
- mat[i][j] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows,cols = len(mat),len(mat[0])
        dp = [[[0 for _ in range(4)] for j in range(cols)]for i in range(rows)]
        long_line = 0
        # dp[0][0] = mat[0][0]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    dp[i][j][0] = dp[i][j-1][0]+1 if j>0 else 1
                    dp[i][j][1] = dp[i-1][j][1]+1 if i>0 else 1
                    dp[i][j][2] = dp[i-1][j-1][2]+1 if i>0 and j>0 else 1
                    dp[i][j][3] = dp[i-1][j+1][3]+1 if i>0 and j<cols-1 else 1
                    long_line =  max(long_line,dp[i][j][0],dp[i][j][1],dp[i][j][2],dp[i][j][3])
        return long_line
```
