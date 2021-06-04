# [Home](./../..)/[Amazon](./..)/[Hard](./)/Largest_Rectangle_in_Histogram
<h1>Largest Rectangle in Histogram</h1>

<p>
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg">

    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg">

    Input: heights = [2,4]
    Output: 4

<b>Constraints:</b>

- 1 <= heights.length <= 105
- 0 <= heights[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        n = len(heights)
        max_area = 0
        for i,h in enumerate(heights):
            while len(st)>1 and heights[st[-1]]>h:
                max_area = max(max_area,heights[st.pop()]*(i-st[-1]-1))
            st.append(i)
        while len(st)!=1:
            max_area = max(max_area,heights[st.pop()]*(n-st[-1]-1))
        return max_area
```
