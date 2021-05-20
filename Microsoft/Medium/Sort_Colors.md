# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Sort_Colors
<h1>Sort Colors</h1>

<p>
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
</p>

<b>Example 1:</b>

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    
<b>Example 2:</b>

    Input: nums = [2,0,1]
    Output: [0,1,2]
    
<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 300
- nums[i] is 0, 1, or 2.

<h2>Solution</h2>

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid = 0,0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
```
