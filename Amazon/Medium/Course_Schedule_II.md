# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Course_Schedule_II
<h1>Course Schedule II</h1>

<p>
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

</p>

<b>Example 1:</b>

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
    
<b>Example 2:</b>

    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

<b>Constraints:</b>

- 1 <= numCourses <= 105
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs prerequisites[i] are unique.

<h2>Solution</h2>

```python
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = defaultdict(list)
        
        indegrees = [0]*numCourses
        
        for pair in prerequisites:
            indegrees[pair[0]]+=1
            courses_map[pair[1]].append(pair[0])
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        output = []        
        counter = 0
        while q:
            u = q.popleft()
            output.append(u)
            counter+=1
            for v in courses_map[u]:
                indegrees[v]-=1
                if indegrees[v] == 0:
                    q.append(v)
        
        if counter != numCourses:
            return []
        return output
```
