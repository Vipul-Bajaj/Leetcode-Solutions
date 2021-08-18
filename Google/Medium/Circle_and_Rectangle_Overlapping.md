# [Home](./../..)/[Google](./..)/[Medium](./)/Circle_and_Rectangle_Overlapping
<h1>Circle and Rectangle Overlapping</h1>

<p>
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
</p>
<p>
Return True if the circle and rectangle are overlapped otherwise return False.
</p>
<p>
In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png">

    Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
    Output: true
    Explanation: Circle and rectangle share the point (1,0) 
    
<b>Example 2:</b>    

<img src="https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png">

    Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
    Output: true
    
<b>Example 3:</b>    

<img src="https://assets.leetcode.com/uploads/2020/03/03/sample_6_1728.png">

    Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
    Output: true

<b>Example 4:</b>    

    Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
    Output: false
    
<b>Constraints:</b>

- 1 <= radius <= 2000
- -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
- x1 < x2
- y1 < y2

<h2>Solution</h2>

```python
class Solution:
    def checkOverlap(self, r: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        corners = [(x1,y1), (x2,y1), (x2,y2), (x1, y2)]
        for (x, y) in corners:
            if (x_center - x)**2 + (y_center - y)**2 <= r**2:
                return True

        for x in [x1, x2]:
            if x_center-r <= x <= x_center+r and y1<=y_center<=y2:
                return True
        for y in [y1, y2]:
            if y_center-r <= y <= y_center+r and x1<=x_center<=x2:
                return True
        return x1<=x_center<=x2 and y1<=y_center<=y2
```
