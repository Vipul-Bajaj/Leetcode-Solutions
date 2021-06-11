# [Home](./../..)/[Facebook](./..)/[Medium](./)/Contiguous_Array
<h1>Contiguous Array</h1>

<p>
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
</p>

<b>Example 1:</b>

    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
    
<b>Example 2:</b>

    Input: nums = [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
    
<b>Constraints:</b>

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0:-1}
        count = 0
        max_len = 0
        for i in range(len(nums)):
            count+=1 if nums[i]==1 else -1
            if count in hm:
                max_len = max(max_len,i-hm[count])
            else:
                hm[count] = i
        return max_len
```
