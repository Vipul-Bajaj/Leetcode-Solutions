<h1>Find First and Last Position of Element in Sorted Array</h1>

<p>
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

</p>

<b>Example 1:</b>

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
<b>Example 2:</b>

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    
<b>Example 3:</b>

    Input: nums = [], target = 0
    Output: [-1,-1]

<b>Constraints:</b>

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array.
- -10^9 <= target <= 10^9

<h2>Solution</h2>

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low,high = 0,n-1
        start,end = -1,-1
        while low<=high:
            mid = (low+high)//2
            
            if (nums[mid] == target and mid == low) or (nums[mid]== target and nums[mid-1]< target):
                start = mid
            if nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        
        low,high = 0,n-1
        while low<=high:
            mid = (low+high)//2
            
            if (nums[mid] == target and mid == high) or (nums[mid]== target and nums[mid+1] > target):
                end = mid
            if nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        
        return [start,end]
```
