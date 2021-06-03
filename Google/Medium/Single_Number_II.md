# [Home](./../..)/[Google](./..)/[Medium](./)/Single_Number_II
<h1>Single Number II</h1>

<p>
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
</p>
<p>
You must implement a solution with a linear runtime complexity and use only constant extra space.
</p>

<b>Example 1:</b>

    Input: nums = [2,2,3,2]
    Output: 3
 
<b>Example 2:</b>

    Input: nums = [0,1,0,1,0,1,99]
    Output: 99

<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each element in nums appears exactly three times except for one element which appears once.

<h2>Solution</h2>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3-sum(nums))//2
```
