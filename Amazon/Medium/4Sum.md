# [Home](./../..)/[Amazon](./..)/[Medium](./)/4Sum
<h1>4Sum</h1>

<p>
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
</p>

<b>Example 1:</b>

    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
<b>Example 2:</b>

    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

<b>Constraints:</b>

- 1 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

<h2>Solution</h2>

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen = dict()
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1,n):
                curr_sum = nums[i] + nums[j]
                diff = target - curr_sum
                if diff in seen:
                    for prev_sum in seen[diff]:
                        if nums[prev_sum[1]] <= nums[i] and i>prev_sum[1]:
                            res.add((nums[prev_sum[0]], nums[prev_sum[1]], nums[i], nums[j]))
                if curr_sum in seen:
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]
        
        return list(res)
```
