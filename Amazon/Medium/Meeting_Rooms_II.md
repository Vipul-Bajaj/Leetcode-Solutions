# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Meeting_Rooms_II
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Meeting_Rooms_II
<h1>Meeting Rooms II</h1>

<p>
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

</p>

<b>Example 1:</b>

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
    
<b>Example 2:</b>

    Input: intervals = [[7,10],[2,4]]
    Output: 1

<b>Constraints:</b>

- 1 <= intervals.length <= 104
- 0 <= starti < endi <= 106

<h2>Solution</h2>

```python
class Solution:
    def _comparator(self,left,right):
        if left[0]>right[0]:
            return 1
        if left[0]<right[0]:
            return -1
        if left[1]>right[1]:
            return -1
        if left[1]<right[1]:
            return 1
        if left[1]==right[1]:
            return 0
        
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        meetings = []
        
        for interval in intervals:
            meetings.append((interval[0],0))
            meetings.append((interval[1],1))
        
        meetings.sort(key=cmp_to_key(self._comparator))
        # print(meetings)
        max_rooms = 0
        for meeting in meetings:
            if meeting[1] == 0:
                rooms+=1
            else:
                rooms-=1
            max_rooms = max(max_rooms,rooms)
        return max_rooms
```
