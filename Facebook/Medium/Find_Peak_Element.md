<h1>Find Peak Element</h1>

<p>
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

<b>Example 2:</b>

    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

<b>Constraints:</b>

- 1 <= nums.length <= 1000
- -231 <= nums[i] <= 231 - 1
- nums[i] != nums[i + 1] for all valid i.

<h2>Solution</h2>

```python
# O(n) solution
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         nums = [-float("inf")] + nums + [-float("inf")]
#         n = len(nums)
#         for i in range(1,n-1):
#             if nums[i-1]<nums[i]>nums[i+1]:
#                 return i-1
# O(logn) solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low,high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low
```
