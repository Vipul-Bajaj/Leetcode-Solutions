# [Home](./../..)/[Facebook](./..)/[Medium](./)/Set_Matrix_Zeroes
<h1>Set Matrix Zeroes</h1>

<p>
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
</p>

<b>Follow up:</b>

* A straight forward solution using O(mn) space is probably a bad idea.
* A simple improvement uses O(m + n) space, but still not the best solution.
* Could you devise a constant space solution?

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg">

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg">

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

<b>Constraints:</b>

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -231 <= matrix[i][j] <= 231 - 1

<h2>Solution</h2>

```python
# O(m+n) space solution
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m,n = len(matrix),len(matrix[0])
#         zeroes = []
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     zeroes.append((i,j))
#         for r,c in zeroes:
#             for i in range(r+1,m):
#                 matrix[i][c] = 0
#             for j in range(c,n):
#                 matrix[r][j] = 0
#             for i in range(r-1,-1,-1):
#                 matrix[i][c] = 0
#             for j in range(c-1,-1,-1):
#                 matrix[r][j] = 0  
#         return matrix
 
# O(1) space solution    
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col=False
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j]=0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
```
