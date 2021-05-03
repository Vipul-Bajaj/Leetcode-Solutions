# [Home](./../../..)/[Google](./../..)/[Hard](./..)/Course_Schedule_III
# [Home](./../../..)/[Google](./../..)/[Hard](./..)/Course_Schedule_III
<h1>Course Schedule III</h1>

<p>
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

</p>

<b>Example 1:</b>

    Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    Output: 3
    Explanation: 
    There are totally 4 courses, but you can take 3 courses at most:
    First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
    Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
    Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
    The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
    
<b>Example 2:</b>

    Input: courses = [[1,2]]
    Output: 1

<b>Example 3:</b>

    Input: courses = [[3,2],[4,3]]
    Output: 0

<b>Constraints:</b>

- 1 <= courses.length <= 104
- 1 <= durationi, lastDayi <= 104

<h2>Solution</h2>

```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses.sort(key = lambda x:(x[1],x[0]))
        sum_so_far = 0
        import heapq
        hq = []
        for course in courses:
            sum_so_far += course[0]
            heapq.heappush(hq, -1*course[0])
            if sum_so_far > course[1]:
                sum_so_far += heapq.heappop(hq)

        return len(hq)
```
