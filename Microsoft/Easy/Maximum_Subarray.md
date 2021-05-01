<h1>Maximum Subarray</h1>

<p>
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

<b>Example 1:</b>

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    
<b>Example 2:</b>

    Input: nums = [1]
    Output: 1
    
<b>Example 3:</b>

    Input: nums = [5,4,-1,7,8]
    Output: 23

<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- -10^5 <= nums[i] <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far = -2**31
        max_ending_here = 0
        
        for i in range(n):
            max_ending_here = max_ending_here + nums[i]
            if max_so_far<max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here<0:
                max_ending_here = 0
        
        return max_so_far
```
