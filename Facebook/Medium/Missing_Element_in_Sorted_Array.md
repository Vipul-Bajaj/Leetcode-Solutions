# [Home](./../..)/[Facebook](./..)/[Medium](./)/Missing_Element_in_Sorted_Array
<h1>Missing Element in Sorted Array</h1>

<p>
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.
</p>

<b>Example 1:</b>

    Input: nums = [4,7,9,10], k = 1
    Output: 5
    Explanation: The first missing number is 5.
    
<b>Example 2:</b>

    Input: nums = [4,7,9,10], k = 3
    Output: 8
    Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
    
<b>Example 3:</b>

    Input: nums = [1,2,4], k = 3
    Output: 6
    Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

<b>Constraints:</b>

- 1 <= nums.length <= 5 * 104
- 1 <= nums[i] <= 107
- nums is sorted in ascending order, and all the elements are unique.
- 1 <= k <= 108

<h2>Solution</h2>

```python
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx:nums[idx]-nums[0]-idx
        
        n = len(nums)
        
        if k>missing(n-1):
            return nums[-1] + k - missing(n-1)
        
        left,right = 0,n-1
        
        while left<right:
            mid = (left+right)//2
            
            if missing(mid)<k:
                left = mid+1
            else:
                right = mid
        
        return nums[left-1]+k-missing(left-1)
```
