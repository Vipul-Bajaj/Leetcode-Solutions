# [Home](./../..)/[Facebook](./..)/[Easy](./)/Meeting_Rooms
<h1>Meeting Rooms</h1>

<p>
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

</p>

<b>Example 1:</b>

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false
    
<b>Example 2:</b>

    Input: intervals = [[7,10],[2,4]]
    Output: true

<b>Constraints:</b>

- 0 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti < endi <= 106

<h2>Solution</h2>

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
```
