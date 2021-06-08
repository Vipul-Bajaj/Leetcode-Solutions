# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Valid_Triangle_Number
<h1>Valid Triangle Number</h1>

<p>
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
</p>

<b>Example 1:</b>

    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid combinations are: 
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3
    
<b>Example 2:</b>

    Input: nums = [4,2,3,4]
    Output: 4

<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-2):
            k = i+2
            j = i+1
            while j<n-1 and nums[i]!=0:
                while k<n and nums[i]+nums[j]>nums[k]:
                    k+=1;
                count+=k-j-1
                j+=1
                
        return count
```
