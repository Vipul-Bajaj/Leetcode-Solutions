# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Container_With_Most_Water
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Container_With_Most_Water
<h1>Container With Most Water</h1>

<p>
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

</p>

<b>Example 1:</b>

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg">

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    
<b>Example 2:</b>

    Input: height = [1,1]
    Output: 1
    
<b>Example 3:</b>

    Input: height = [4,3,2,1,4]
    Output: 16

<b>Constraints:</b>

- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        n= len(height)
        i,j = 0,n-1
        while i<j:
            area = min(height[i],height[j])*(j-i)
            max_area = max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area
```
