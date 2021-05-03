# [Home](./../..)/[Amazon](./..)/[Medium](./)/Number_of_Provinces
<h1>Number of Provinces</h1>

<p>
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg">

    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg">

    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

<b>Constraints:</b>

- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

<h2>Solution</h2>

```python
# DFS Approach
class Solution:
    def dfs(self,isConnected,u,visited,n):
        visited[u] = 1
        
        for v in range(n):
            if not visited[v] and isConnected[u][v] == 1:
                self.dfs(isConnected,v,visited,n)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = [0]*n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces+=1
                self.dfs(isConnected,i,visited,n)
                
        return provinces

# BFS Approach
from collections import deque
class Solution:
    def bfs(self,isConnected,u,visited,n):
        q = deque()
        q.append(u)
        while q:
            u = q.popleft()
            visited[u] = 1
            for v in range(n):
                if not visited[v] and isConnected[u][v] == 1:
                    q.append(v)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visited = [0]*n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces+=1
                self.bfs(isConnected,i,visited,n)
                
        return provinces
```
