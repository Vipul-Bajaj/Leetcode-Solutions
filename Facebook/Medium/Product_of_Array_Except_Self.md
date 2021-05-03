# [Home](./../..)/[Facebook](./..)/[Medium](./)/Product_of_Array_Except_Self
<h1>Product of Array Except Self</h1>

<p>
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    
<b>Example 2:</b>

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

<b>Constraints:</b>

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

<h2>Solution</h2>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        ans[0] = 1
        
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
            
        R = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i]*R
            R*=nums[i]
        
        return ans
```
