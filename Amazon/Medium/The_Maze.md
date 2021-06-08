# [Home](./../..)/[Amazon](./..)/[Medium](./)/The_Maze
<h1>The Maze</h1>

<p>
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
</p>
<p>
Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
</p>
<p>
You may assume that the borders of the maze are all walls (see examples).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-1-grid.jpg">

    Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
    Output: true
    Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/31/maze1-2-grid.jpg">

    Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
    Output: false
    Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

<b>Example 3:</b>

    Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
    Output: false
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
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m,n = len(maze),len(maze[0])
        
        visited = [[False for j in range(n)] for i in range(m)]
        dirs = [[0, 1] ,[0, -1], [-1, 0], [1, 0]]
        visited[start[0]][start[1]] = True
        
        q = deque([start])
        while q:
            pos = q.popleft()
            if pos[0] == destination[0] and pos[1]==destination[1]:
                return True
            for dx,dy in dirs:
                x = pos[0]+dx
                y = pos[1]+dy
                while x>=0 and x<m and y>=0 and y<n and maze[x][y] == 0:
                    x+=dx
                    y+=dy
                if not visited[x-dx][y-dy]:
                    visited[x-dx][y-dy]=True
                    q.append([x-dx,y-dy])
        return False
```
