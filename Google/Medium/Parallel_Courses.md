# [Home](./../..)/[Google](./..)/[Medium](./)/Parallel_Courses
<h1>Parallel Courses</h1>

<p>
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
</p>
<p>
In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.
</p>
<p>
Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/24/course1graph.jpg">

    Input: n = 3, relations = [[1,3],[2,3]]
    Output: 2
    Explanation: The figure above represents the given graph.
    In the first semester, you can take courses 1 and 2.
    In the second semester, you can take course 3.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/24/course2graph.jpg">

    Input: n = 3, relations = [[1,2],[2,3],[3,1]]
    Output: -1
    Explanation: No course can be studied because they are prerequisites of each other.
    
<b>Constraints:</b>

- 1 <= n <= 5000
- 1 <= relations.length <= 5000
- relations[i].length == 2
- 1 <= prevCoursei, nextCoursei <= n
- prevCoursei != nextCoursei
- All the pairs [prevCoursei, nextCoursei] are unique.

<h2>Solution</h2>

```python
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        courses_map = defaultdict(list)
        
        indegrees = [0]*(n+1)
        
        for pair in relations:
            indegrees[pair[1]]+=1
            courses_map[pair[0]].append(pair[1])
        
        q = deque()
        for i in range(1,n+1):
            if indegrees[i] == 0:
                q.append(i)
        if not q:
            return -1
        q.append(None)
        counter = 0
        sem = 0
        while q:
            u = q.popleft()
            if u:
                counter+=1
                for v in courses_map[u]:
                    indegrees[v]-=1
                    if indegrees[v] == 0:
                        q.append(v)
            else:
                sem+=1
                if q:
                    q.append(None)
        if counter != n:
            return -1
        return sem
```
