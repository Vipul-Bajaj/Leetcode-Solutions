<h1>Combination Sum IV</h1>

<p>
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    Note that different sequences are counted as different combinations.
    
<b>Example 2:</b>

    Input: nums = [9], target = 3
    Output: 0

<b>Constraints:</b>

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

<h2>Solution</h2>

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for j in range(n):
                if nums[j]<=i:
                    dp[i] += dp[i-nums[j]]

        # print(dp)
        return dp[target]
```
