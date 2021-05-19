# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Minimum_Moves_to_Equal_Array_Elements_II
<h1>Minimum Moves to Equal Array Elements II</h1>

<p>
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: 2
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
    
<b>Example 2:</b>

    Input: nums = [1,10,2,9]
    Output: 16
    
<b>Constraints:</b>

- n == nums.length
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n%2==0:
            mid = (nums[(n//2)-1]+nums[n//2])//2
        else:
            mid = nums[n//2]
        ans = 0
        for num in nums:
            ans+=abs(mid-num)
        return ans
```
