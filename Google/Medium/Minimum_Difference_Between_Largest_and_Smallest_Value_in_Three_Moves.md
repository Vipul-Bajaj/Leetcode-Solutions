# [Home](./../..)/[Google](./..)/[Medium](./)/Minimum_Difference_Between_Largest_and_Smallest_Value_in_Three_Moves
<h1>Minimum Difference Between Largest and Smallest Value in Three Moves</h1>

<p>
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
</p>
<p>
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.
</p>

<b>Example 1:</b>

    Input: nums = [5,3,2,4]
    Output: 0
    Explanation: Change the array [5,3,2,4] to [2,2,2,2].
    The difference between the maximum and minimum is 2-2 = 0.

<b>Example 2:</b>

    Input: nums = [1,5,0,10,14]
    Output: 1
    Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
    The difference between the maximum and minimum is 1-0 = 1.

<b>Example 3:</b>

    Input: nums = [6,6,0,1,1,4,6]
    Output: 2

<b>Example 4:</b>

    Input: nums = [1,5,6,14,15]
    Output: 1
<b>Constraints:</b>

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

<h2>Solution</h2>

```python
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n<5:
            return 0
        res = float("inf")
        
        for i in range(4):
            res = min(res, nums[n-4+i]-nums[i])
        return res
```
