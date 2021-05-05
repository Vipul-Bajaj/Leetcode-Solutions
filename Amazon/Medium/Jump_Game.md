# [Home](./../..)/[Amazon](./..)/[Medium](./)/Jump_Game
<h1>Jump Game</h1>

<p>
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

</p>

<b>Example 1:</b>

    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
<b>Example 2:</b>

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    
<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- 0 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n-1
        for i in range(n-1,-1,-1):
            if i+nums[i]>=last:
                last = i
        return last==0
```
