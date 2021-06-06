# [Home](./../..)/[Amazon](./..)/[Easy](./)/Search_Insert_Position
<h1>Search Insert Position</h1>

<p>
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
</p>

<b>Example 1:</b>

    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
<b>Example 2:</b>

    Input: nums = [1,3,5,6], target = 2
    Output: 1

<b>Example 3:</b>

    Input: nums = [1,3,5,6], target = 7
    Output: 4

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

<h2>Solution</h2>

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)
        while low<high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid
        return low
```
