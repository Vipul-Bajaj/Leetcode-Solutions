# [Home](./../..)/[Zillow](./..)/[Medium](./)/Max_Consecutive_Ones_II
<h1>Max Consecutive Ones II</h1>

<p>
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
</p>

<b>Example 1:</b>

    Input: nums = [1,0,1,1,0]
    Output: 4
    Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
    
<b>Example 2:</b>

    Input: nums = [1,0,1,1,0,1]
    Output: 4

<b>Constraints:</b>

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_c = 0
        zeroes = 0
        l,r = 0,0
        while r<n:
            if nums[r] == 0:
                zeroes+=1
            while zeroes == 2:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            max_c = max(max_c,r-l+1)
            r+=1
        return max_c
```
