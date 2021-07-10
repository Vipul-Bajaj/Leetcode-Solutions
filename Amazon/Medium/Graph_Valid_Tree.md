# [Home](./../..)/[Amazon](./..)/[Medium](./)/Graph_Valid_Tree
<h1>Graph Valid Tree</h1>

<p>
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
</p>
<p>
Return true if the edges of the given graph make up a valid tree, and false otherwise.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg">

    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg">

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false

<b>Constraints:</b>

- 1 <= 2000 <= n
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

<h2>Solution</h2>

```python
class Solution:
    def hasCycle(self,graph,visited,node,parent):
        visited[node] = True
        
        for child in graph[node]:
            if not visited[child]:
                if self.hasCycle(graph,visited,child,node):
                    return True
            elif child!=parent:
                return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
        visited = [False]*n
        if self.hasCycle(graph,visited,0,-1):
            return False
        
        return visited.count(True)==n
```
