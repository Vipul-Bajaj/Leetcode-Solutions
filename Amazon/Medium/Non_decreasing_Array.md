# [Home](./../..)/[Amazon](./..)/[Medium](./)/Non_decreasing_Array
<h1>Non-decreasing Array</h1>

<p>
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

</p>

<b>Example 1:</b>

    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
    
<b>Example 2:</b>

    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.

<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 104
- -105 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                if count == 1:
                    return False
                count+=1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True
```
