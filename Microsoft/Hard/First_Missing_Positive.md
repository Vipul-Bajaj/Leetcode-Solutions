# [Home](./../../..)/[Microsoft](./../..)/[Hard](./..)/First_Missing_Positive
<h1>First Missing Positive</h1>

<p>
Given an unsorted integer array nums, find the smallest missing positive integer.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,0]
    Output: 3
    
<b>Example 2:</b>

    Input: nums = [3,4,-1,1]
    Output: 2
    
<b>Example 3:</b>

    Input: nums = [7,8,9,11,12]
    Output: 1

<b>Constraints:</b>

- 0 <= nums.length <= 300
- -2^31 <= nums[i] <= 2^31 - 1

<h2>Solution</h2>

```python
# O(nlogn) approach    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive = 1
        nums = sorted(set(nums))
        for i in nums:
            if i>0:
                if i == positive:
                    positive+=1
                else:
                    return positive

        return positive
    
# O(n) approach    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        if n ==1:
            return 2
    
        nums = [i if i>0 and i<=n else 1 for i in nums]
        
        for i in range(n):
            a = abs(nums[i])
            
            if a == n:
                nums[0] = -1 * abs(nums[0])
            else:
                nums[a] = -1 * abs(nums[a])
                
        for i in range(1,n):
            if nums[i]>0:
                return i
        
        if nums[0]>0:
            return n
        
        return n+1
```
