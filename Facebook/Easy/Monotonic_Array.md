# [Home](./../..)/[Facebook](./..)/[Easy](./)/Monotonic_Array
<h1>Monotonic Array</h1>

<p>
An array is monotonic if it is either monotone increasing or monotone decreasing.
</p>
<p>
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
</p>
<p>  
Return true if and only if the given array nums is monotonic.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,2,3]
    Output: true
    
<b>Example 2:</b>

    Input: nums = [6,5,4,4]
    Output: true
    
<b>Example 3:</b>

    Input: nums = [1,3,2]
    Output: false

<b>Constraints:</b>

- 1 <= nums.length <= 50000
- -100000 <= nums[i] <= 100000

<h2>Solution</h2>

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = dec = True
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inc = False
            if nums[i]<nums[i+1]:
                dec = False
        return inc or dec
```
