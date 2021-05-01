<h1>Course Schedule</h1>

<p>
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

<b>Example 1:</b>

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    
<b>Example 2:</b>

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

<b>Constraints:</b>

- 1 <= numCourses <= 105
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

<h2>Solution</h2>

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = defaultdict(list)
        
        indegrees = [0]*numCourses
        
        for pair in prerequisites:
            indegrees[pair[0]]+=1
            courses_map[pair[1]].append(pair[0])
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        counter = 0
        while q:
            u = q.popleft()
            counter+=1
            for v in courses_map[u]:
                indegrees[v]-=1
                if indegrees[v] == 0:
                    q.append(v)
        
        if counter != numCourses:
            return False
        return True
```
