# [Home](./../..)/[Facebook](./..)/[Medium](./)/Single_Number_III
<h1>Single Number III</h1>

<p>
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
</p>
<p>
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]
    Explanation:  [5, 3] is also a valid answer.

<b>Example 2:</b>

    Input: nums = [-1,0]
    Output: [-1,0]
    
<b>Example 3:</b>

    Input: nums = [0,1]
    Output: [1,0]
    
<b>Constraints:</b>

- 2 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each integer in nums will appear twice, only two integers will appear once.

<h2>Solution</h2>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        xor = 0
        for n in nums:
            xor^=n
        out = []
        for n in nums:
            if xor^n in nums:
                out.append(xor^n)
        return out
```
