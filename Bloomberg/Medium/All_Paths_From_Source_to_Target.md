# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/All_Paths_From_Source_to_Target
<h1>All Paths From Source to Target</h1>

<p>
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
</p>
<p>
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg">

    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg">

    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    
<b>Example 3:</b>

    Input: graph = [[1],[]]
    Output: [[0,1]]

<b>Constraints:</b>

- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops).
- The input graph is guaranteed to be a DAG.

<h2>Solution</h2>

```python
class Solution:
    def dfs(self,node,graph,paths,path,n):
        if node == n:
            paths.append(path.copy())
            return
        for child in graph[node]:
            path.append(child)
            self.dfs(child,graph,paths,path,n)
            del path[-1]
        return 
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(0,graph,paths,[0],len(graph)-1)
        return paths
```
