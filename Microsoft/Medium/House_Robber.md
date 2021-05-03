# [Home](./../..)/[Microsoft](./..)/[Medium](./)/House_Robber
<h1>House Robber</h1>

<p>
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
    
<b>Example 2:</b>

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

<b>Constraints:</b>

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

<h2>Solution</h2>

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        excl = 0
        incl = 0
        for i in nums:
            new_excl = excl if excl>incl else incl
            incl = excl+i
            excl = new_excl
        return excl if excl>incl else incl
```
