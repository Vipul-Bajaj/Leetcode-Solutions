# [Home](./../..)/[Amazon](./..)/[Medium](./)/Find_All_Duplicates_in_an_Array
<h1>Find All Duplicates in an Array</h1>

<p>
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

</p>

<b>Example 1:</b>

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [2,3]
    
<b>Example 2:</b>

    Input: nums = [1,1,2]
    Output: [1]
    
<b>Example 3:</b>

    Input: nums = [1]
    Output: []

<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 105
- 1 <= nums[i] <= n
- Each element in nums appears once or twice.

<h2>Solution</h2>

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        for i in range(n):
            if nums[abs(nums[i])%n]<0:
                out.append(n if abs(nums[i])%n==0 else abs(nums[i])%n)
            nums[abs(nums[i])%n] = -nums[abs(nums[i])%n]
        return out
```
