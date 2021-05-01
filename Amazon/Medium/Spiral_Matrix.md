<h1>Spiral Matrix</h1>

<p>
Given an m x n matrix, return all elements of the matrix in spiral order.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg">

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
  
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg">

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
<b>Constraints:</b>

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100


<h2>Solution</h2>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = 0
        m,n = len(matrix), len(matrix[0])
        t,b,l,r= 0,m,0,n
        flat_list = []
        while t<b and l<r:
            if d==0:
                for i in range(l,r):
                    flat_list+=[matrix[t][i]]
                d = 1
                t+=1
            elif d==1:
                for i in range(t,b):
                    flat_list+=[matrix[i][r-1]]
                d = 2
                r-=1
            elif d==2:
                for i in range(r-1,l-1,-1):
                    flat_list+=[matrix[b-1][i]]
                d = 3
                b-=1
            elif d==3:
                for i in range(b-1,t-1,-1):
                    flat_list+=[matrix[i][l]]
                d = 0
                l+=1
                
        return flat_list
```
