# [Home](./../..)/[Amazon](./..)/[Easy](./)/Single_Number
<h1>Single Number</h1>

<p>
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
</p>

<b>Example 1:</b>

    Input: nums = [2,2,1]
    Output: 1
    
<b>Example 2:</b>

    Input: nums = [4,1,2,1,2]
    Output: 4

<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- -3 * 104 <= nums[i] <= 3 * 104
- Each element in the array appears twice except for one element which appears only once.

<h2>Solution</h2>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans^=i
        return ans
```
