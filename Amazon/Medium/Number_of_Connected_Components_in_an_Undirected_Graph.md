# [Home](./../..)/[Amazon](./..)/[Medium](./)/Number_of_Connected_Components_in_an_Undirected_Graph
<h1>Number of Connected Components in an Undirected Graph</h1>

<p>
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg">

    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg">

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

<b>Constraints:</b>

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

<h2>Solution</h2>

```python
class Solution:
    def dfs(self, u, adj_list,visited):
        visited[u] = 1
        
        for v in adj_list[u]:
            if not visited[v]:
                self.dfs(v, adj_list,visited)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        visited = [0]*n
        for i in range(n):
            adj_list[i] = []
        
        for pair in edges:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
        
        components = 0
        for i in range(n):
            if not visited[i]:
                components+=1
                self.dfs(i,adj_list,visited)
        
        return components
```
