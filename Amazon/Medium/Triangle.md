<h1>Triangle</h1>

<p>
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

<b>Example 1:</b>

    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
    
<b>Example 2:</b>

    Input: triangle = [[-10]]
    Output: -10

<b>Constraints:</b>

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -104 <= triangle[i][j] <= 104

<h2>Solution</h2>

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(m-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]) 
        return triangle[0][0]
```
