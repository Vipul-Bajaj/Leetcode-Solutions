<h1>Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts</h1>

<p>
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png">

    Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
    Output: 4 
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_3.png">

    Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
    Output: 6
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
    
<b>Example 3:</b>

    Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
    Output: 9
    
<b>Constraints:</b>

- 2 <= h, w <= 10^9
- 1 <= horizontalCuts.length < min(h, 10^5)
- 1 <= verticalCuts.length < min(w, 10^5)
- 1 <= horizontalCuts[i] < h
- 1 <= verticalCuts[i] < w
- It is guaranteed that all elements in horizontalCuts are distinct.
- It is guaranteed that all elements in verticalCuts are distinct.

<h2>Solution</h2>

```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max([horizontalCuts[i]-horizontalCuts[i-1] for i in range(1,len(horizontalCuts))])
        max_v = max([verticalCuts[i]-verticalCuts[i-1] for i in range(1,len(verticalCuts))])
        
        return (max_h*max_v)%(10**9+7)
```
