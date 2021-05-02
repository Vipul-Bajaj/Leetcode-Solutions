<h1>3Sum Closest</h1>

<p>
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
</p>

<b>Example 1:</b>

    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

<b>Constraints:</b>

- 3 <= nums.length <= 10^3
- -10^3 <= nums[i] <= 10^3
- -10^4 <= target <= 10^4

<h2>Solution</h2>

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        p_closest = 2**31-1
        n_closest = -2**31
        ans = set()
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == target:
                    return target
                elif nums[i]+nums[j]+nums[k]-target<0:
                    n_closest = max(n_closest,nums[i]+nums[j]+nums[k])
                    j+=1
                else:
                    p_closest = min(p_closest,nums[i]+nums[j]+nums[k])
                    k-=1
        
        return p_closest if abs(n_closest-target)>p_closest-target else n_closest
```
