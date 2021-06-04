# [Home](./../..)/[Amazon](./..)/[Hard](./)/Trapping_Rain_Water
<h1>Trapping Rain Water</h1>

<p>
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png">

    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    
<b>Example 2:</b>

    Input: height = [4,2,0,3,2,5]
    Output: 9

<b>Constraints:</b>

- n == height.length
- 0 <= n <= 3 * 104
- 0 <= height[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        lm,rm = 0,0
        l,r = 0,n-1
        result = 0
        while l<=r:
            if height[l]<height[r]:
                if height[l]>lm:
                    lm = height[l]
                else:
                    result+=lm-height[l]
                l+=1
            else:
                if height[r]>rm:
                    rm = height[r]
                else:
                    result+=rm-height[r]
                r-=1
        return result
```
