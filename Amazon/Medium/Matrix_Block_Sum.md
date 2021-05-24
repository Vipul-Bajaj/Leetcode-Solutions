# [Home](./../..)/[Amazon](./..)/[Medium](./)/Matrix_Block_Sum
<h1>Matrix Block Sum</h1>

<p>
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
</p>

* i - k <= r <= i + k,
* j - k <= c <= j + k, and

<p>
(r, c) is a valid position in the matrix.
</p>

<b>Example 1:</b>

    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[12,21,16],[27,45,33],[24,39,28]]
    
<b>Example 2:</b>

    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
    Output: [[45,45,45],[45,45,45],[45,45,45]]

<b>Constraints:</b>

- m == mat.length
- n == mat[i].length
- 1 <= m, n, k <= 100
- 1 <= mat[i][j] <= 100

<h2>Solution</h2>

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = mat[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i == 0:
                    dp[i][j] = mat[i][j]+dp[i][j-1]
                elif j == 0:
                    dp[i][j] = mat[i][j]+dp[i-1][j]
                else:
                    dp[i][j] = mat[i][j]+dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
        for i in range(m):
            row_upper = max(0,i-k)
            row_lower = min(m-1,i+k)
            for j in range(n):
                col_left = max(0,j-k)
                col_right = min(n-1,j+k)
                value = dp[row_lower][col_right]
                if row_upper-1>=0:
                    value-=dp[row_upper-1][col_right]
                if col_left-1>=0:
                    value-=dp[row_lower][col_left-1]
                if row_upper-1>=0 and col_left-1>=0:
                    value+=dp[row_upper-1][col_left-1]
                mat[i][j] = value
        return mat
```
