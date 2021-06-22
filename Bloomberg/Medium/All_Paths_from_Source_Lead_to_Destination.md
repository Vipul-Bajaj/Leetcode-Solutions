# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/All_Paths_from_Source_Lead_to_Destination
<h1>All Paths from Source Lead to Destination</h1>

<p>
Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:
</p>

* At least one path exists from the source node to the destination node
* If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
* The number of possible paths from source to destination is a finite number.

<p>
Return true if and only if all roads from source lead to destination.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/16/485_example_1.png">

    Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
    Output: false
    Explanation: It is possible to reach and get stuck on both node 1 and node 2.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/16/485_example_2.png">

    Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
    Output: false
    Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
    

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/16/485_example_3.png">

    Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
    Output: true
    
<b>Example 4:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/16/485_example_4.png">

    Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
    Output: false
    Explanation: All paths from the source node end at the destination node, but there are an infinite number of paths, such as 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1-1-2, and so on.

<b>Example 5:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/16/485_example_5.png">

    Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
    Output: false
    Explanation: There is infinite self-loop at destination node.

<b>Constraints:</b>

- 1 <= n <= 104
- 0 <= edges.length <= 104
- edges.length == 2
- 0 <= ai, bi <= n - 1
- 0 <= source <= n - 1
- 0 <= destination <= n - 1
- The given graph may have self-loops and parallel edges.

<h2>Solution</h2>

```python
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)
        visited = defaultdict(int)
        for [x,y] in edges:
            g[x].add(y)
                
        def dfs(node):
            if visited[node] == 1:
                return True
            elif visited[node] == -1:
                return False
            elif len(g[node]) == 0:
                return node==destination
            else:
                visited[node] = -1
                for child in g[node]:
                    if not dfs(child):
                        return False
                visited[node] = 1
                return True
        
        return dfs(source)
```
