# [Home](./../..)/[Google](./..)/[Medium](./)/Non_overlapping_Intervals
<h1>Non-overlapping Intervals</h1>

<p>
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
</p>

<b>Example 1:</b>

    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    
<b>Example 2:</b>    

    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    
<b>Example 3:</b>     

    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

<b>Constraints:</b>

- 1 <= intervals.length <= 2 * 104
- intervals[i].length == 2
- -2 * 104 <= starti < endi <= 2 * 104

<h2>Solution</h2>

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l = 0
        ls,le = intervals[0]
        for s,e in intervals[1:]:
            if s<le:
                if e<le:
                    ls,le = s,e
                l+=1
            else:
                ls,le = s,e
        return l
```
