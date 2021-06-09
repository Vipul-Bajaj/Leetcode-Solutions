# [Home](./../..)/[Google](./..)/[Medium](./)/Wiggle_Sort
<h1>Wiggle Sort</h1>

<p>
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
<br>
You may assume the input array always has a valid answer.
</p>

<b>Example 1:</b>

    Input: nums = [3,5,2,1,6,4]
    Output: [3,5,1,6,2,4]
    Explanation: [1,6,2,5,3,4] is also accepted.
  
<b>Example 2:</b>

    Input: nums = [6,6,5,6,3,8]
    Output: [6,6,5,6,3,8]
 
<b>Constraints:</b>

* 1 <= nums.length <= 5 * 104
* 0 <= nums[i] <= 104
* It is guaranteed that there will be an answer for the given input nums.

<h2>Solution</h2>

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if (i%2==0) == (nums[i]>nums[i+1]):
                nums[i],nums[i+1] = nums[i+1],nums[i]
        return numsd(interval)
        return st
```
