# [Home](./../..)/[Google](./..)/[Medium](./)/Remove_Interval
<h1>Remove Interval</h1>

<p>
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).
</p>
<p>
You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.
</p>
<p>
Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/removeintervalex1.png">

    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    Output: [[0,1],[6,7]]

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/removeintervalex2.png">

    Input: intervals = [[0,5]], toBeRemoved = [2,3]
    Output: [[0,2],[3,5]]

<b>Example 3:</b>

    Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
    Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
    
<b>Constraints:</b>

- 1 <= intervals.length <= 104
- -109 <= ai < bi <= 109

<h2>Solution</h2>

```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        output = []
        rs,re = toBeRemoved
        for s,e in intervals:
            if s>re or e<rs:
                output.append([s,e])
            else:
                if s<rs:
                    output.append([s,rs])
                if e>re:
                    output.append([re,e])
        return output
```
