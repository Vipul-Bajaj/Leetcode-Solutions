# [Home](./../..)/[Google](./..)/[Medium](./)/Valid_Square
<h1>Valid Square</h1>

<p>
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
</p>
<p>
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
</p>
<p>
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
</p>

<b>Example 1:</b>

    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: true

<b>Example 2:</b>

    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
    Output: false

<b>Example 3:</b>

    Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
    Output: true
<b>Constraints:</b>

- p1.length == p2.length == p3.length == p4.length == 2
- -104 <= xi, yi <= 104

<h2>Solution</h2>

```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = sorted([p1,p2,p3,p4])
        def dist(p1,p2):
            return (p2[1]-p1[1])*(p2[1]-p1[1])+(p2[0]-p1[0])*(p2[0]-p1[0])
        
        return dist(points[0],points[1])!=0 and dist(points[0],points[1]) == dist(points[1],points[3]) and dist(points[1],points[3]) == dist(points[3],points[2]) and dist(points[3],points[2]) == dist(points[2],points[0]) and dist(points[0],points[3]) == dist(points[2],points[1])
```
