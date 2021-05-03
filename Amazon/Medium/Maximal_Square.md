# [Home](./../..)/[Amazon](./..)/[Medium](./)/Maximal_Square
<h1>Maximal Square</h1>

<p>
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

</p>

<b>Example 1:</b>

    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4
    
<b>Example 2:</b>

    Input: matrix = [["0","1"],["1","0"]]
    Output: 1
    
<b>Example 3:</b>

    Input: matrix = [["0"]]
    Output: 0

<b>Constraints:</b>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.

<h2>Solution</h2>

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0 for j in range(n)]for i in range(m)]
        max_till = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j]=="1":
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0

        max_till = max(map(max, dp))
        return max_till*max_till
```
