# [Home](./../..)/[Yandex](./..)/[Medium](./)/Line_Reflection
<h1>Line Reflection</h1>

<p>
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, in other words, answer whether or not if there exists a line that after reflecting all points over the given line the set of the original points is the same that the reflected ones.

Note that there can be repeated points.

Follow up:

Could you do better than O(n2) ?
</p>

<b>Example 1:</b>

    Input: points = [[1,1],[-1,1]]
    Output: true
    Explanation: We can choose the line x = 0.
    
<b>Example 2:</b>

    Input: points = [[1,1],[-1,-1]]
    Output: false
    Explanation: We can't choose a line.

<b>Constraints:</b>

- n == points.length
- 1 <= n <= 10^4
- -10^8 <= points[i][j] <= 10^8

<h2>Solution</h2>

```python
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        min_x = points[0][0]
        max_x = points[0][0]
        points_set = set()
        for point in points:
            min_x = min(min_x,point[0])
            max_x = max(max_x,point[0])
            points_set.add(tuple(point))
        for point in points:
            if (min_x+max_x-point[0],point[1]) not in points_set:
                return False
        return True
```
