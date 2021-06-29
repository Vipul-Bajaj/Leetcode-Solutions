# [Home](./../..)/[Facebook](./..)/[Medium](./)/Max_Consecutive_Ones_III
<h1>Max Consecutive Ones III</h1>

<p>
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
</p>

<b>Example 1:</b>

    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    
<b>Example 2:</b>

    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

<b>Constraints:</b>

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

<h2>Solution</h2>

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_c = 0
        zeroes = 0
        l,r = 0,0
        while r<n:
            if nums[r] == 0:
                zeroes+=1
            while zeroes == k+1:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            max_c = max(max_c,r-l+1)
            r+=1
        return max_c
```
