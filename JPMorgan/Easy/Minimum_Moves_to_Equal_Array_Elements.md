<h1>Minimum Moves to Equal Array Elements</h1>

<p>
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: 3
    Explanation: Only three moves are needed (remember each move increments two elements):
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    
<b>Example 2:</b>

    Input: nums = [1,1,1]
    Output: 0

<b>Constraints:</b>

- n == nums.length
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = min(nums)
        ans = 0
        for i in nums:
            ans+=i-_min
        return ans
```
