# [Home](./../..)/[Amazon](./..)/[Medium](./)/Rotated_Sorted_Array
<h1>Rotated Sorted Array</h1>

<p>
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

</p>

<b>Example 1:</b>

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
  
<b>Example 2:</b>

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

<b>Example 3:</b>

    Input: nums = [1], target = 0
    Output: -1
 
<b>Constraints:</b>

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is guaranteed to be rotated at some pivot.
    -10^4 <= target <= 10^4


<h2>Solution</h2>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        
        while low<=high:
            mid = (low+high)//2
            
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1    
        return -1
```
