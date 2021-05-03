# [Home](./../..)/[Facebook](./..)/[Medium](./)/Interval_List_Intersections
<h1>Interval List Intersections</h1>

<p>
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
</p>
<p>
Return the intersection of these two interval lists.
</p>
<p>
A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.
</p>
<p>
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png">

    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    
<b>Example 2:</b>

    Input: firstList = [[1,3],[5,9]], secondList = []
    Output: []
    
<b>Example 3:</b>

    Input: firstList = [[1,7]], secondList = [[3,10]]
    Output: [[3,7]]

<b>Constraints:</b>

- 0 <= firstList.length, secondList.length <= 1000
- firstList.length + secondList.length >= 1
- 0 <= starti < endi <= 109
- endi < starti+1
- 0 <= startj < endj <= 109
- endj < startj+1

<h2>Solution</h2>

```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        firstList.sort()
        secondList.sort()
        output = []
        i,j = 0,0
        while i<m and j<n:
            s1,e1 = firstList[i]
            s2,e2 = secondList[j]
            if e1<s2:
                i+=1
            elif e2<s1:
                j+=1
            else:
                s,e = max(s1,s2),min(e1,e2)
                output.append([s,e])
                if e1<e2:
                    i+=1
                else:
                    j+=1
        return output
```
