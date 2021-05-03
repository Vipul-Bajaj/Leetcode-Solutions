# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Course_Schedule_IV
<h1>Course Schedule IV</h1>

<p>
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether the course uj is a prerequisite of the course vj or not. Note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

Return a boolean array answer, where answer[j] is the answer of the jth query.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg">

    Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
    Output: [false,true]
    Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.
    
<b>Example 2:</b>

    Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
    Output: [false,false]
    Explanation: There are no prerequisites and each course is independent.

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg">

    Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
    Output: [true,true]

<b>Constraints:</b>

- 2 <= numCourses <= 100
- 0 <= prerequisite.length <= (numCourses * (numCourses - 1) / 2)
- 0 <= ai, bi < n
- ai != bi
- All the pairs [ai, bi] are unique.
- The prerequisites graph has no cycles.
- 1 <= queries.length <= 104
- 0 <= ui, vi < n
- ui != vi

<h2>Solution</h2>

```python
class Solution:
    def dfs(self,adj_list,visited,start,target):
        if start in adj_list:
            for child in adj_list[start]:
                if child in visited:
                    continue
                if child == target:
                    return True
                visited.add(child)
                if self.dfs(adj_list,visited,child,target):
                    return True
        return False
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = {}
        for edge in prerequisites:
            if edge[1] in adj_list:
                adj_list[edge[1]].append(edge[0])
            else:
                adj_list[edge[1]] = [edge[0]]
        out = []                
        for u,v in queries:
            if v not in adj_list:
                out.append(False)
                continue
            out.append(self.dfs(adj_list, set(), v, u))
        return out
```
