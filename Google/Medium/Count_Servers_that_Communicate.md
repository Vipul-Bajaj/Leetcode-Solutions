# [Home](./../..)/[Google](./..)/[Medium](./)/Count_Servers_that_Communicate
<h1>Count Servers that Communicates</h1>

<p>
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
</p>
<p>
Return the number of servers that communicate with any other server.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg">

    Input: grid = [[1,0],[0,1]]
    Output: 0
    Explanation: No servers can communicate with others.
  
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg">

    Input: grid = [[1,0],[1,1]]
    Output: 3
    Explanation: All three servers can communicate with at least one other server.

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg">

    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
<b>Constraints:</b>

* m == grid.length
* n == grid[i].length
* 1 <= m <= 250
* 1 <= n <= 250
* grid[i][j] == 0 or 1

<h2>Solution</h2>

```python
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (sum(grid[i]) > 1 or sum(grid[x][j] for x in range(row)) > 1):
                    ans += 1
        return ans
```
