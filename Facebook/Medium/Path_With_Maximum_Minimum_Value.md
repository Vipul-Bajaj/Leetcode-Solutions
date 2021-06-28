# [Home](./../..)/[Facebook](./..)/[Medium](./)/Path_With_Maximum_Minimum_Value
<h1>Path With Maximum Minimum Value</h1>

<p>
Given a matrix of integers grid with m rows and n columns, find the maximum score of a path starting at [0,0] and ending at [m-1,n-1].
</p>
<p>
The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.
</p>
<p>
A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).
</p>

<b>Example 1:</b>

    Input: [[5,4,5],[1,2,6],[7,4,6]]
    Output: 4
    Explanation: 
    The path with the maximum score is highlighted in yellow. 
    
<b>Example 2:</b>

    Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
    Output: 2
 
<b>Example 3:</b>

    Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    Output: 3 

<b>Constraints:</b>

- 1 <= m, n <= 100
0 <= grid[i][j] <= 109

<h2>Solution</h2>

```python
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set((0,0))
        q = [(-grid[0][0],[0,0])]
        score = grid[0][0]
        while q:
            val,pos = heapq.heappop(q)
            x,y = pos
            score = min(score,-val)
            if x == m-1 and y == n-1:
                return score
            for nx,ny in [[x,y+1],[x,y-1],[x-1,y],[x+1,y]]:
                if nx<0 or nx>=m or ny<0 or ny>=n or (nx,ny) in visited:
                    continue
                visited.add((nx,ny))
                heapq.heappush(q,(-grid[nx][ny],[nx,ny]))
```
