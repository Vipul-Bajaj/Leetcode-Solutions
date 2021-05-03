# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Next_Permutation
# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Next_Permutation
<h1>Next Permutation</h1>

<p>
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: [1,3,2]
    
<b>Example 2:</b>

    Input: nums = [3,2,1]
    Output: [1,2,3]
    
<b>Example 3:</b>

    Input: nums = [1,1,5]
    Output: [1,5,1]

<b>Constraints:</b>

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

<h2>Solution</h2>

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j = n-1
            while j>=0 and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        j = n-1
        i = i+1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
```
