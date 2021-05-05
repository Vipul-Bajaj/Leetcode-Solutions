# [Home](./../..)/[Amazon](./..)/[Medium](./)/Jump_Game_II
<h1>Jump Game II</h1>

<p>
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

</p>

<b>Example 1:</b>

    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
<b>Example 2:</b>

    Input: nums = [2,3,0,1,4]
    Output: 2

<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        curr_jump_end = 0
        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            if i==curr_jump_end:
                jumps+=1
                curr_jump_end = farthest
        
        return jumps
```
