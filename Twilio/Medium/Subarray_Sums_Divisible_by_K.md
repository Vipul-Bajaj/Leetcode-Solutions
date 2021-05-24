# [Home](./../..)/[Twilio](./..)/[Medium](./)/Subarray_Sums_Divisible_by_K
<h1>Subarray Sums Divisible by K</h1>

<p>
Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.
</p>

<b>Example 1:</b>

    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

<b>Constraints:</b>

- 1 <= nums.length <= 30000
- -10000 <= nums[i] <= 10000
- 2 <= k <= 10000

<h2>Solution</h2>

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in nums:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res
```
