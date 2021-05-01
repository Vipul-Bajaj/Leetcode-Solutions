<h1>Two Sum</h1>

<p>
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

<b>Example 1:</b>

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    
<b>Example 2:</b>

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
<b>Example 3:</b>

    Input: nums = [3,3], target = 6
    Output: [0,1]

<b>Constraints:</b>

- 2 <= nums.length <= 103
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

<h2>Solution</h2>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]],i]
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
```
