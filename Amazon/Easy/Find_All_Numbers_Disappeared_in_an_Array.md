# [Home](./../..)/[Amazon](./..)/[Easy](./)/Find_All_Numbers_Disappeared_in_an_Array
<h1>Find All Numbers Disappeared in an Array</h1>

<p>
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
</p>

<b>Example 1:</b>

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]
    
<b>Example 2:</b>

    Input: nums = [1,1]
    Output: [2]

<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 105
- 1 <= nums[i] <= n

<h2>Solution</h2>

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        for i in range(n):
            nums[abs(nums[i])%n] = -1*abs(nums[abs(nums[i])%n])
        for idx,num in enumerate(nums):
            if num>0:
                if idx == 0:
                    out.append(n)
                else:
                    out.append(idx)
        return out
```
