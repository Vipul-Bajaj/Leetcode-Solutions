# [Home](./../../..)/[Amazon](./../..)/[Hard](./..)/Critical_Connections_in_a_Network
# [Home](./../../..)/[Amazon](./../..)/[Hard](./..)/Critical_Connections_in_a_Network
<h1>Critical Connections in a Network</h1>

<p>
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png">

    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.

<b>Constraints:</b>

- 1 <= n <= 10^5
- n-1 <= connections.length <= 10^5
- connections[i][0] != connections[i][1]
- There are no repeated connections.

<h2>Solution</h2>

```python
class Solution:
    def cut_edges(self,u):
        self.visited[u] = True
        self.low[u] = self.num
        self.dfsnum[u] = self.num
        self.num+=1
        
        for v in self.adj_list[u]:
            if self.visited[v] == False:
                self.parent[v]=u
                self.cut_edges(v)
                
                if self.low[v]>self.dfsnum[u]:
                    self.ans.append([u,v])
                self.low[u] = min(self.low[u],self.low[v])
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u],self.dfsnum[v])
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.adj_list = defaultdict(list)
    
        for u,v in connections:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

        self.low = [float("Inf")] * n
        self.dfsnum = [float("Inf")] * n
        self.visited = [False] * n
        self.num = 0
        self.parent = [-1] * n
        self.ans = []
        
        for i in range(n):
            if self.visited[i] == False:
                self.cut_edges(i)
        
        return self.ans
```
