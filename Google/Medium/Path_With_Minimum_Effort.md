# [Home](./../..)/[Google](./..)/[Medium](./)/Path_With_Minimum_Effort
<h1>Path With Minimum Effort</h1>

<p>
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
</p>
<p>
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
</p>
<p>
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/04/ex1.png">

    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
    This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
    
<b>Example 2:</b>    

<img src="https://assets.leetcode.com/uploads/2020/10/04/ex2.png">

    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
    
<b>Example 3:</b>     

<img src="https://assets.leetcode.com/uploads/2020/10/04/ex3.png">

    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: This route does not require any effort.

<b>Constraints:</b>

- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 106

<h2>Solution</h2>

```python
class Solution:   
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        
        def bfs(mid):
            visited = [[False for j in range(cols)]for i in range(rows)]
            
            q = deque([(0,0)])
            while q:
                x,y = q.popleft()
                if x == rows-1 and y == cols-1:
                    return True
                visited[x][y] = True
                for nx,ny in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if nx<0 or nx>=rows or ny<0 or ny>=cols or visited[nx][ny]:
                        continue
                    curr_diff = abs(heights[nx][ny]-heights[x][y])
                    if curr_diff<=mid:
                        visited[nx][ny] = True
                        q.append([nx,ny])
            
            
        left,right = 0,10**6
        while left<right:
            mid = (left+right)//2
            if bfs(mid):
                right = mid
            else:
                left = mid+1
        return left
```
