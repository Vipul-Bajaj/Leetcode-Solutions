# [Home](./../..)/[Google](./..)/[Medium](./)/Insert_Interval
<h1>Insert Interval</h1>

<p>
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
<br>
You may assume that the intervals were initially sorted according to their start times.
</p>

<b>Example 1:</b>

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
  
<b>Example 2:</b>

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

<b>Example 3:</b>

    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]
 
<b>Constraints:</b>

* 0 <= intervals.length <= 104
* intervals[i].length == 2
* 0 <= intervals[i][0] <= intervals[i][1] <= 105
* intervals is sorted by intervals[i][0] in ascending order.
* newInterval.length == 2
* 0 <= newInterval[0] <= newInterval[1] <= 105

<h2>Solution</h2>

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect_left(intervals,newInterval)
        intervals.insert(index,newInterval)
        st = []
        for interval in intervals:
            if st and st[-1][1]>=interval[0]:
                intt = st.pop()
                st.append([intt[0],max(intt[1],interval[1])])
                continue
            st.append(interval)
        return st
```
