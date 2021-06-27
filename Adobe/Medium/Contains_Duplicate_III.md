# [Home](./../..)/[Adobe](./..)/[Medium](./)/Contains_Duplicate_III
<h1>Contains Duplicate III</h1>

<p>
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true
    
<b>Example 2:</b>

    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true
    
<b>Example 3:</b>    

    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
    
<b>Constraints:</b>

- 0 <= nums.length <= 2 * 104
- -231 <= nums[i] <= 231 - 1
- 0 <= k <= 104
- 0 <= t <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w]
        return False
```
