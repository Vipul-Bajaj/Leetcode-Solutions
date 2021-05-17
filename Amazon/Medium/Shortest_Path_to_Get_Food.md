# [Home](./../..)/[Amazon](./..)/[Medium](./)/Shortest_Path_to_Get_Food
<h1>Shortest Path to Get Food</h1>

<p>
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:
</p>

* '*' is your location. There is exactly one '*' cell.
* '#' is a food cell. There may be multiple food cells.
* 'O' is free space, and you can travel through these cells.
* 'X' is an obstacle, and you cannot travel through these cells.

<p>
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/img1.jpg">

    Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    Output: 3
    Explanation: It takes 3 steps to reach the food.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/img2.jpg">

    Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
    Output: -1
    Explanation: It is not possible to reach the food.
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/img3.jpg">

    Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
    Output: 6
    Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

<b>Constraints:</b>

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[row][col] is '*', 'X', 'O', or '#'.
- The grid contains exactly one '*'.

<h2>Solution</h2>

```python
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = deque([])
        m,n = len(grid),len(grid[0])
        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i,j))
                    found = True
                    break
            if found:
                break
        
        min_steps = 0
        while q:
            min_steps+=1
            for _ in range(len(q)):
                pos = q.popleft()
                for x,y in [[-1,0],[0,-1],[1,0],[0,1]]:
                    i = pos[0]+x
                    j = pos[1]+y
                    if 0<=i<m and 0<=j<n and grid[i][j] != 'X':
                        if grid[i][j] == '#':
                            return min_steps
                        elif grid[i][j] == 'O':
                            grid[i][j] = 'X'
                            q.append((i,j))
        
        return -1
```
