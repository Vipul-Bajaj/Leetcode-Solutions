# [Home](./../..)/[Amazon](./..)/[Medium](./)/Redundant_Connection
<h1>Redundant Connection</h1>

<p>
In this problem, a tree is an undirected graph that is connected and has no cycles.
</p>
<p>
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
</p>
<p>
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg">

    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg">

    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

<b>Constraints:</b>

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

<h2>Solution</h2>

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
```
