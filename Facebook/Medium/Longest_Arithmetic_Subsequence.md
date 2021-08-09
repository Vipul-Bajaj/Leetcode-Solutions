# [Home](./../..)/[Facebook](./..)/[Medium](./)/Longest_Arithmetic_Subsequence
<h1>Longest Arithmetic Subsequence</h1>

<p>
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
</p>
<p>
Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
</p>

<b>Example 1:</b>

    Input: nums = [3,6,9,12]
    Output: 4
    Explanation: 
    The whole array is an arithmetic sequence with steps of length = 3.

<b>Example 2:</b>

    Input: nums = [9,4,7,2,10]
    Output: 3
    Explanation: 
    The longest arithmetic subsequence is [4,7,10].
  
<b>Example 3:</b>

    Input: nums = [20,1,15,3,10,5,8]
    Output: 4
    Explanation: 
    The longest arithmetic subsequence is [20,15,10,5].

<b>Constraints:</b>

- 2 <= nums.length <= 1000
- 0 <= nums[i] <= 500

<h2>Solution</h2>

```python
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dp[j, nums[j] - nums[i]] = dp.get((i, nums[j] - nums[i]), 1) + 1
        return max(dp.values())
```
