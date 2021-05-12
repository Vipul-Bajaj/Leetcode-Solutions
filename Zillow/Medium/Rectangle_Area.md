# [Home](./../..)/[Zillow](./..)/[Medium](./)/Rectangle_Area
<h1>Rectangle Area</h1>

<p>
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png">

    Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
    Output: 45
    
<b>Example 2:</b>

    Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
    Output: 16

<b>Constraints:</b>

- -104 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 104

<h2>Solution</h2>

```python
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax2-ax1)*abs(ay2-ay1)
        area2 = abs(bx2-bx1)*abs(by2-by1)
        x1,y1 = max(ax1,bx1),max(ay1,by1)
        x2,y2 = min(ax2,bx2),min(ay2,by2)
        overlap = 0
        if x2-x1>0 and y2-y1>0:
            overlap = (x2-x1)*(y2-y1)
        return area1+area2-overlap
```
