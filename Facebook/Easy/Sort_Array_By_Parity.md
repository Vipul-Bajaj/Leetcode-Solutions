# [Home](./../..)/[Facebook](./..)/[Easy](./)/Sort_Array_By_Parity
<h1>Sort Array By Parity</h1>

<p>
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.
</p>

<b>Example 1:</b>

    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

<b>Constraints:</b>

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

<h2>Solution</h2>

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        
        while l<r:
            if l<n and nums[l]%2==0:
                l+=1
            if r>-1 and nums[r]%2==1:
                r-=1
            if l<r:
                nums[l],nums[r] = nums[r],nums[l]
        
        return nums
```
