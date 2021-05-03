# [Home](./../..)/[Amazon](./..)/[Easy](./)/Two_Sum_Less_Than_K
<h1>Two Sum Less Than K</h1>

<p>
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

</p>

<b>Example 1:</b>

    Input: nums = [34,23,1,24,75,33,54,8], k = 60
    Output: 58
    Explanation: We can use 34 and 24 to sum 58 which is less than 60.
    
<b>Example 2:</b>

    Input: nums = [10,20,30], k = 15
    Output: -1
    Explanation: In this case it is not possible to get a pair sum less that 15.
    
<b>Constraints:</b>

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 1000
- 1 <= k <= 2000

<h2>Solution</h2>

```python
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        n = len(nums)
        nums.sort()
        i,j = 0,n-1
        while i<j:
            s = nums[i]+nums[j]
            if s<k:
                max_sum = max(max_sum,s)
                i+=1
            else:
                j-=1
        return max_sum
```
