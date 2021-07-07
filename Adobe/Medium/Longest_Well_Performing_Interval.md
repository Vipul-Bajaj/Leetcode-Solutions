# [Home](./../..)/[Adobe](./..)/[Medium](./)/Longest_Well_Performing_Interval
<h1>Longest Well-Performing Interval</h1>

<p>
We are given hours, a list of the number of hours worked per day for a given employee.
</p>
<p>
A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
</p>
<p>
A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
</p>
<p>
Return the length of the longest well-performing interval.
</p>

<b>Example 1:</b>

    Input: hours = [9,9,6,0,6,6,9]
    Output: 3
    Explanation: The longest well-performing interval is [9,9,6].
    
<b>Constraints:</b>

- 1 <= hours.length <= 10000
- 0 <= hours[i] <= 16

<h2>Solution</h2>

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_int,ntv,seen = 0,0,{}
        for idx,hr in enumerate(hours):
            ntv+=1 if hr>8 else -1
            if ntv>0:
                max_int = idx+1
            else:
                if ntv not in seen:
                    seen[ntv] = idx
                if ntv-1 in seen:
                    max_int = max(max_int,idx-seen[ntv-1])
        return max_int
```
