# [Home](./../..)/[Facebook](./..)/[Medium](./)/Maximum_Size_Subarray_Sum_Equals_k
<h1>Maximum Size Subarray Sum Equals k</h1>

<p>
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
</p>

<b>Example 1:</b>

    Input: nums = [1,-1,5,-2,3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

<b>Example 2:</b>

    Input: nums = [-2,-1,2,1], k = 1
    Output: 2
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.

<b>Constraints:</b>

- 1 <= nums.length <= 2 * 105
- -104 <= nums[i] <= 104
- -109 <= k <= 109

<h2>Solution</h2>

```python
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans, acc = 0, 0               
        mp = {0:-1}                
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i 
            if acc-k in mp:
                ans = max(ans, i-mp[acc-k])
        return ans
```
