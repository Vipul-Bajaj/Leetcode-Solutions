# [Home](./../..)/[Amazon](./..)/[Medium](./)/Search_in_Rotated_Sorted_Array_II
<h1>Search in Rotated Sorted Array II</h1>

<p>
There is an integer array nums sorted in ascending order (not necessarily with distinct values).
</p>
<p>
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
</p>
<p>
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
</p>

<b>Example 1:</b>

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
  
<b>Example 2:</b>

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false
 
<b>Constraints:</b>
- 1 <= nums.length <= 5000
- -104 <= nums[i] <= 104
- nums is guaranteed to be rotated at some pivot.
- -104 <= target <= 104

<h2>Solution</h2>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1
        
        while low<=high:
            mid = (low+high)//2
            
            if nums[mid]==target:
                return True
            while low < mid and nums[low] == nums[mid]: # tricky part
                low += 1
            if nums[low]<=nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1    
        return False
```
