# [Home](./../..)/[Apple](./..)/[Medium](./)/Increasing_Subsequences
<h1>Increasing Subsequences</h1>

<p>
Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.
</p>
<p>
The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.
</p>

<b>Example 1:</b>

    Input: nums = [4,6,7,7]
    Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    
<b>Example 2:</b>

    Input: nums = [4,4,3,2,1]
    Output: [[4,4]]

<b>Constraints:</b>

- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100

<h2>Solution</h2>

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, nums):
            if( len(curr) >= 2 and curr[-1] < curr[-2] ): return
            if( len(curr) >= 2 and curr[:] not in result):
                result.add(curr[:])
            for i in range(len(nums)):
                backtrack( curr + (nums[i],), nums[i+1:] )  # using tuples for curr instead of list
        result = set()
        backtrack( (), nums)
        return result
```
