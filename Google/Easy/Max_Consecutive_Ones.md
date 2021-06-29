# [Home](./../..)/[Google](./..)/[Easy](./)/Max_Consecutive_Ones
<h1>Max Consecutive Ones</h1>

<p>
Given a binary array nums, return the maximum number of consecutive 1's in the array.
</p>

<b>Example 1:</b>

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    
<b>Example 2:</b>

    Input: nums = [1,0,1,1,0,1]
    Output: 2

<b>Constraint:</b>
- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max_c = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                max_c = max(max_c,c)
                c = 0     
        return max(max_c,c)
```
