<h1>Pascal's Triangle</h1>

<p>
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif">

<b>Example 1:</b>

    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
<b>Example 2:</b>

    Input: numRows = 1
    Output: [[1]]
    
<b>Constraints:</b>

- 1 <= numRows <= 30

<h2>Solution</h2>

```python
from math import ceil
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows== 1:
            return [[1]]
        ans = [[1],[1,1]]
        for i in range(2,numRows):
            l = [1]
            for j in range(1,ceil((i+1)/2)):
                l.append(ans[i-1][j-1]+ans[i-1][j])
            if i%2==0:
                l = l[:-1] + l[::-1]
            else:
                l = l + l[::-1]
            ans.append(l)
        return ans
```
