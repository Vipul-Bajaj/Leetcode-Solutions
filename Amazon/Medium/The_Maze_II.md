# [Home](./../..)/[Amazon](./..)/[Medium](./)/The_Maze_II
<h1>The Maze II</h1>

<p>
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
</p>
<p>
Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.
</p>
<p>
The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
</p>  
<p>
You may assume that the borders of the maze are all walls (see examples).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-1-grid.jpg">

    Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
    Output: 12
    Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-2-grid.jpg">

    Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
    Output: -1
    Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

<b>Example 3:</b>

    Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
    Output: -1
<b>Constraints:</b>

- m == maze.length
- n == maze[i].length
- 1 <= m, n <= 100
- maze[i][j] is 0 or 1.
- start.length == 2
- destination.length == 2
- 0 <= startrow, destinationrow <= m
- 0 <= startcol, destinationcol <= n
- Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
- The maze contains at least 2 empty spaces.

<h2>Solution</h2>

```python
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        
        dp = [[float("inf") for j in range(n)] for i in range(m)]
        dirs = [[0, 1] ,[0, -1], [-1, 0], [1, 0]]
        dp[start[0]][start[1]] = 0
        
        q = deque([start])
        while q:
            pos = q.popleft()
            
            for dx,dy in dirs:
                x = pos[0]+dx
                y = pos[1]+dy
                c = 0
                while x>=0 and x<m and y>=0 and y<n and maze[x][y] == 0:
                    x+=dx
                    y+=dy
                    c+=1
                if dp[pos[0]][pos[1]]+c<dp[x-dx][y-dy]:
                    dp[x-dx][y-dy]=dp[pos[0]][pos[1]]+c
                    q.append([x-dx,y-dy])
        return -1 if dp[destination[0]][destination[1]] == float("inf") else dp[destination[0]][destination[1]]
```
