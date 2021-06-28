# [Home](./../..)/[Amazon](./..)/[Medium](./)/Find_Minimum_in_Rotated_Sorted_Array
<h1>Find Minimum in Rotated Sorted Array</h1>

<p>
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
</p>
<p>
  
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
  
<p>  
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
</p>
<p>
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
</p>
<p>
You must write an algorithm that runs in O(log n) time.
</p>

<b>Example 1:</b>

    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
  
<b>Example 2:</b>

    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

<b>Example 3:</b>

    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
<b>Constraints:</b>
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.

<h2>Solution</h2>

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if (left==right) or (nums[mid-1]>nums[mid] and nums[mid+1]>nums[mid]):
                return nums[mid]
            elif nums[mid]>=nums[left] and nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid-1
```
