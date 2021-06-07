# [Home](./../..)/[Amazon](./..)/[Medium](./)/01_Matrix
<h1>01_Matrix</h1>

<p>
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
<br>
The distance between two adjacent cells is 1.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg">

    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg">

    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]

<b>Constraints:</b>

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 104
- 1 <= m * n <= 104
- mat[i][j] is either 0 or 1.
- There is at least one 0 in mat.

<h2>Solution</h2>

```python
# BFS Approach
# class Solution:
#     def bfs(self,mat,i,j,m,n,dp):
#         q = deque([((i,j),0)])
#         visited = set([(i,j)])
#         while q:
#             pos,step = q.popleft()
#             i,j = pos
#             if mat[i][j]==0:
#                 return step
#             for dx,dy in [[-1,0],[0,-1],[0,1],[1,0]]:
#                 new_i = i+dx
#                 new_j = j+dy
#                 if 0<=new_i<m and 0<=new_j<n and (new_i,new_j) not in visited:
#                     visited.add((new_i,new_j))
#                     q.append(((new_i,new_j),step+1))
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m,n = len(mat),len(mat[0])
        
#         dp = [[0 for j in range(n)]for i in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] != 0:
#                     dp[i][j] = self.bfs(mat,i,j,m,n,dp)
        
#         return dp

# DP Approach
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix
```
