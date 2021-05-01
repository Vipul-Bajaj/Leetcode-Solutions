<h1>Pascal's Triangle II</h1>

<p>
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif">

</p>

<b>Example 1:</b>

    Input: rowIndex = 3
    Output: [1,3,3,1]
    
<b>Example 2:</b>

    Input: rowIndex = 0
    Output: [1]
    
<b>Example 3:</b>

    Input: rowIndex = 1
    Output: [1,1]

<b>Constraints:</b>

- 0 <= rowIndex <= 33

<h2>Solution</h2>

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        
        pascal_row = []

        res=1
        for i in range(0,n+1):
            pascal_row.append(res)
            res*=(n-i)
            res//=(i+1)
            
        return pascal_row
```
