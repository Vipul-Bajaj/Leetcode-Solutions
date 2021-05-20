# [Home](./../..)/[Facebook](./..)/[Medium](./)/Spiral_Matrix_III
<h1>Spiral Matrix III</h1>

<p>
On a 2 dimensional grid with rows rows and cols columns, we start at (rStart, cStart) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all rows * cols spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.
</p>

<b>Example 1:</b>

    Input: rows = 1, cols = 4, rStart = 0, cStart = 0
    Output: [[0,0],[0,1],[0,2],[0,3]]
    
<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png">    
    
<b>Example 2:</b>

    Input: rows = 5, cols = 6, rStart = 1, cStart = 4
    Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png">

<b>Constraints:</b>

- 1 <= rows <= 100
- 1 <= cols <= 100
- 0 <= rStart < rows
- 0 <= cStart < cols

<h2>Solution</h2>

```python
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        dx, dy, n = 0, 1, 0
        while len(res) < rows * cols:
            for i in range(n // 2 + 1):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                rStart, cStart = rStart + dx, cStart + dy
            dx, dy, n = dy, -dx, n + 1
        return res
```
