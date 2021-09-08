# [Home](./../..)/[Facebook](./..)/[Hard](./)/Best_Meeting_Point
<h1>Best Meeting Point</h1>

<p>
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.
</p>
<p>
The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
</p>
<p>
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/meetingpoint-grid.jpg">

    Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    Output: 6
    Explanation: Given three friends living at (0,0), (0,4), and (2,2).
    The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
    So return 6.

<b>Example 2:</b>

    Input: grid = [[1,1]]
    Output: 1
<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is either 0 or 1.
- There will be at least two friends in the grid.

<h2>Solution</h2>

```python
class Solution:
    def minDistance(self, points, origin):
        dist = 0
        for x in points:
            dist+=abs(x-origin)
        return dist
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        rows, cols = [],[]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    rows.append(row)
                    
        for col in range(n):
            for row in range(m):
                if grid[row][col] == 1:
                    cols.append(col)
        
        row, col = rows[len(rows)//2],cols[len(cols)//2]
        
        return self.minDistance(rows, row)+ self.minDistance(cols,col)
```
