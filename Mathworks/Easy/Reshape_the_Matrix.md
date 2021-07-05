# [Home](./../..)/[Mathworks](./..)/[Easy](./)/Reshape_the_Matrix
<h1>Reshape the Matrix</h1>

<p>
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
</p>
<p>
You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.
</p>
<p>
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
</p>
<p>
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg">

    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg">

    Input: mat = [[1,2],[3,4]], r = 2, c = 4
    Output: [[1,2],[3,4]]

<b>Constraint:</b>
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- -1000 <= mat[i][j] <= 1000
- 1 <= r, c <= 300

<h2>Solution</h2>

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        
        if m*n != r*c:
            return mat
        
        new_mat = [[0 for j in range(c)]for i in range(r)]
        k,l = 0,0
        for i in range(m):
            for j in range(n):
                new_mat[k][l] = mat[i][j]
                l+=1
                if l == c:
                    k+=1
                    l=0
        return new_mat
```
