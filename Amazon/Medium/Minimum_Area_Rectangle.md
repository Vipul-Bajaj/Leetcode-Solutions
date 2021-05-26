# [Home](./../..)/[Amazon](./..)/[Medium](./)/Minimum_Area_Rectangle
<h1>Minimum Area Rectangle</h1>

<p>
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.
</p>

<b>Example 1:</b>

    Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: 4
    
<b>Example 2:</b>

    Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    Output: 2

<b>Constraints:</b>

- 1 <= points.length <= 500
- 0 <= points[i][0] <= 40000
- 0 <= points[i][1] <= 40000
- All points are distinct.

<h2>Solution</h2>

```python
cclass Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0
```
