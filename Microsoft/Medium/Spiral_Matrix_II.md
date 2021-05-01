<h1>Spiral Matrix II</h1>

<p>
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

</p>

<b>Example 1:</b>

    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
    
<b>Example 2:</b>

    Input: n = 1
    Output: [[1]]

<b>Constraints:</b>

- 1 <= n <= 20

<h2>Solution</h2>

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)]for i in range(n)]
        d = 0
        m = n
        t,b,l,r= 0,m,0,n
        ele = 1
        while t<b and l<r:
            if d==0:
                for i in range(l,r):
                    matrix[t][i] = ele
                    ele+=1
                d = 1
                t+=1
            elif d==1:
                for i in range(t,b):
                    matrix[i][r-1] = ele
                    ele+=1
                d = 2
                r-=1
            elif d==2:
                for i in range(r-1,l-1,-1):
                    matrix[b-1][i] = ele
                    ele+=1
                d = 3
                b-=1
            elif d==3:
                for i in range(b-1,t-1,-1):
                    matrix[i][l] = ele
                    ele+=1
                d = 0
                l+=1
```
