# [Home](./../..)/[Facebook](./..)/[Medium](./)/Diagonal_Traverse
<h1>Diagonal Traverse</h1>

<p>
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg">

    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    
<b> Example 2:</b>
    
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]

<b>Constraints:</b>

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 104
- 1 <= m * n <= 104
- -105 <= mat[i][j] <= 105
<h2>Solution</h2>

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        
        out = deque([])
        up = True
        r,c= 0,0
        while r<m and c<n:
            out.append(mat[r][c])
            nr = r + (-1 if up else 1 )
            nc = c + (1 if up else -1 )
            
            if nr<0 or nr == m or nc<0 or nc==n:
                if up:
                    r += (c == n-1)
                    c += (c < n-1)
                else:
                    c += (r == m-1)
                    r += (r<m-1)
                up = not up
            else:
                r = nr
                c = nc
             
        return out
```
