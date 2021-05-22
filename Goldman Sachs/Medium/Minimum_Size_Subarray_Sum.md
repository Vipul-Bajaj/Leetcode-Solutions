# [Home](./../..)/[Goldman Sachs](./..)/[Medium](./)/Minimum_Size_Subarray_Sum
<h1>Minimum Size Subarray Sum</h1>

<p>
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
</p>

<b>Example 1:</b>

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint. 

<b>Example 2:</b>

    Input: target = 4, nums = [1,4,4]
    Output: 1
    
<b>Example 3:</b>

    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
    
<b>Constraints:</b>

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 2**31-1
        n = len(nums)
        s = 0
        left = 0
        for i in range(n):
            s += nums[i]
            while s>= target:
                min_len = min(min_len,i+1-left)
                s-= nums[left]
                left+=1
        return min_len if min_len != 2**31-1 else 0
```
