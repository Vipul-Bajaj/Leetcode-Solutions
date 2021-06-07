# [Home](./../..)/[Facebook](./..)/[Medium](./)/Maximum_Width_Ramp
<h1>Maximum Width Ramp</h1>

<p>
Given an array nums of integers, a ramp is a tuple (i, j) for which i < j and nums[i] <= nums[j].  The width of such a ramp is j - i.
<br>
Find the maximum width of a ramp in nums.  If one doesn't exist, return 0.
</p>

<b>Example 1:</b>

    Input: nums = [6,0,8,2,1,5]
    Output: 4
    Explanation: 
    The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
    
<b>Example 2:</b>

    Input: nums = [9,8,1,0,1,9,4,0,4,1]
    Output: 7
    Explanation: 
    The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

<b>Constraints:</b>

- 2 <= nums.length <= 50000
- 0 <= nums[i] <= 50000

<h2>Solution</h2>

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0
        for i, a in enumerate(nums):
            if not s or nums[s[-1]] > a:
                s.append(i)
        for j in range(len(nums))[::-1]:
            while s and nums[s[-1]] <= nums[j]:
                res = max(res, j - s.pop())
        return res
```
