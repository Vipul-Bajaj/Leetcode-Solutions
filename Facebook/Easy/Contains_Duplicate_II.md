# [Home](./../..)/[Facebook](./..)/[Easy](./)/Contains_Duplicate_II
<h1>Contains Duplicate II</h1>

<p>
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,1], k = 3
    Output: true
    
<b>Example 2:</b>

    Input: nums = [1,0,1,1], k = 1
    Output: true
    
<b>Example 3:</b>

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

<b>Constraints:</b>

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109
- 0 <= k <= 105

<h2>Solution</h2>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i,n in enumerate(nums):
            if n in hm:
                if abs(i-hm[n])<=k:
                    return True
            hm[n]=i    
        return False
```
