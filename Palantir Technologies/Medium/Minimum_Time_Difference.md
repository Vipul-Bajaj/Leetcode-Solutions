# [Home](./../..)/[Palantir Technologies](./..)/[Medium](./)/Minimum_Time_Difference
<h1>Minimum Time Difference</h1>

<p>
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
</p>

<b>Example 1:</b>

    Input: timePoints = ["23:59","00:00"]
    Output: 1

<b>Example 2:</b>

    Input: timePoints = ["00:00","23:59","00:00"]
    Output: 0
    
<b>Constraints:</b>

- 2 <= timePoints <= 2 * 104
- timePoints[i] is in the format "HH:MM".

<h2>Solution</h2>

```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h,m = time.split(":")
            mi = int(h)*60+int(m)
            minutes.append(mi)
        minutes.sort()
        min_diff = 1440-(minutes[-1]-minutes[0])
        for i in range(1,len(minutes)):
            min_diff = min(min_diff,minutes[i]-minutes[i-1])
        return min_diff
```
