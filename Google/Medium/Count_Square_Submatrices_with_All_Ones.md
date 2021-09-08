# [Home](./../..)/[Google](./..)/[Medium](./)/Count_Square_Submatrices_with_All_Ones
<h1>Count Square Submatrices with All Ones</h1>

<p>
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
</p>

<b>Example 1:</b>

    Input: matrix =
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    Output: 15
    Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

<b>Example 2:</b>

    Input: matrix = 
    [
      [1,0,1],
      [1,1,0],
      [1,1,0]
    ]
    Output: 7
    Explanation: 
    There are 6 squares of side 1.  
    There is 1 square of side 2. 
    Total number of squares = 6 + 1 = 7.
    
<b>Constraints:</b>

- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

<h2>Solution</h2>

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        hm = defaultdict(int)
        m,n = len(matrix),len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=1:
                    continue
                if i == 0 or j == 0:
                    ans+=1
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                    ans+=matrix[i][j]
        return ans
```
