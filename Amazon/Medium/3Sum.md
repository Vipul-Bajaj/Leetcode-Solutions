<h1>3Sum</h1>

<p>
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

<b>Example 1:</b>

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    
<b>Example 2:</b>

    Input: nums = []
    Output: []
    
<b>Example 3:</b>

    Input: nums = [0]
    Output: []

<b>Constraints:</b>

- 0 <= nums.length <= 3000
- -105 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3:
            return []
        nums.sort()
        ans = set()
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    if (nums[i],nums[j],nums[k]) not in ans:
                        ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                else:
                    k-=1
        
        return [list(x) for x in ans]
```
