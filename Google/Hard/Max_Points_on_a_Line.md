# [Home](./../..)/[Google](./..)/[Hard](./)/Max_Points_on_a_Line
<h1>Max Points on a Line</h1>

<p>
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg">

    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg">

    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

<b>Constraints:</b>

- 1 <= points.length <= 300
- points[i].length == 2
- -104 <= xi, yi <= 104
- All the points are unique.

<h2>Solution</h2>

```python
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        max_points = 0
        for i in range(len(points)):
            x1,y1 = points[i]
            hash_map = defaultdict(int)
            hash_map['90'] = 1
            same = 0
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                y_delta = y1-y2
                x_delta = x1-x2
                if y1==y2 and x1==x2:
                    same+=1
                    continue
                elif x1==x2:
                    slope = '90'
                elif y1==y2:
                    slope = '180'
                else:
                    if y_delta<0:
                        x_delta,y_delta = -x_delta,-y_delta
                    gcd = math.gcd(y_delta,x_delta)
                    slope = (y_delta/gcd,x_delta/gcd)
                hash_map[slope] = hash_map.get(slope,1)+1
            max_points = max(max_points,max(hash_map.values())+same)
       
        return max_points
```
