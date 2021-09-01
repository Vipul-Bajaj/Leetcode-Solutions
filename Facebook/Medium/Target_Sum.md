# [Home](./../..)/[Facebook](./..)/[Medium](./)/Target_Sum
<h1>Target Sum</h1>

<p>
You are given an integer array nums and an integer target.
</p>
<p>
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
</p>

- For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

<p>
Return the number of different expressions that you can build, which evaluates to target.
</p>

<b>Example 1:</b>

    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

<b>Example 2:</b>

    Input: nums = [1], target = 1
    Output: 1

<b>Constraints:</b>

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000

<h2>Solution</h2>

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = Counter({0:1})
        for x in nums:
            step = Counter()
            for y in count:
                step[y+x] += count[y]
                step[y-x] += count[y]
            count = step
        return count[target]
```
