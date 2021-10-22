# [Home](./../..)/[Google](./..)/[Hard](./)/Minimum_Cost_to_Make_at_Least_One_Valid_Path_in_a_Grid
<h1>Minimum Cost to Make at Least One Valid Path in a Grid</h1>

<p>
Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
</p>

- 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
- 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
- 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
- 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

<p>
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.
</p>
<p>
You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.
</p>
<p>
You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
</p>
<p>
Return the minimum cost to make the grid have at least one valid path.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/02/13/grid1.png">

    Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    Output: 3
    Explanation: You will start at point (0, 0).
    The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
    The total cost = 3.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/02/13/grid2.png">

    Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
    Output: 0
    Explanation: You can follow the path from (0, 0) to (2, 2).

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/02/13/grid3.png">

    Input: grid = [[1,2],[4,3]]
    Output: 1

<b>Example 4:</b>

    Input: grid = [[2,2,2],[2,2,2]]
    Output: 3

<b>Example 5:</b>

    Input: grid = [[4]]
    Output: 0

<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100

<h2>Solution</h2>

```python
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        
        def neighbourhood(x,y):
            if y+1 < n:
                yield x,y+1, int(grid[x][y]!=1)
            if y-1 >= 0:
                yield x,y-1, int(grid[x][y]!=2)
            if x+1 < m:
                yield x+1,y, int(grid[x][y]!=3)
            if x-1 >= 0:
                yield x-1,y, int(grid[x][y]!=4)
        
        min_cost = defaultdict(lambda: math.inf, {(0,0):0})
        q = deque([(0,0,0)])
        
        while q:
            x,y,cost = q.popleft()
            
            if cost != min_cost[x,y]:
                continue
            if x == m-1 and y == n-1:
                return cost
            
            for nx,ny,step_cost in neighbourhood(x,y):
                if (cost2 := cost + step_cost) < min_cost[nx, ny]:
                    min_cost[nx,ny] = cost2
                    if step_cost:
                        q.append((nx,ny,cost2))
                    else:
                        q.appendleft((nx,ny,cost2))
        return 0
```
