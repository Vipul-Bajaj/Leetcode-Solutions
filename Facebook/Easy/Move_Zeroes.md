# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Move_Zeroes
# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Move_Zeroes
<h1>Move Zeroes</h1>

<p>
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

</p>

<b>Example 1:</b>

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
<b>Example 2:</b>

    Input: nums = [0]
    Output: [0]

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = i
        while i<n and j<n:
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            else:
                j+=1
        return nums
```
