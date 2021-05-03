# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Shortest_Path_in_Binary_Matrix
<h1>Shortest Path in Binary Matrix</h1>

<p>
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/18/example1_1.png">

    Input: grid = [[0,1],[1,0]]
    Output: 2
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/18/example2_1.png">

    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4
    
<b>Example 3:</b>

    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1

<b>Constraints:</b>

- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

<h2>Solution</h2>

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        
        while q:
            row,col = q.popleft()
            dist = grid[row][col]
            if (row,col) == (n-1,n-1):
                return dist
            for d in dirs:
                new_i = row+d[0]
                new_j = col+d[1]
                if 0<=new_i<n and 0<=new_j<n and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = dist+1
                    q.append((new_i,new_j))
        return -1
```
