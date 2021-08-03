# [Home](./../..)/[Honeywell](./..)/[Easy](./)/Minimum_Distance_to_the_Target_Element
<h1>Minimum Distance to the Target Element</h1>

<p>
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
</p>
<p>
Return abs(i - start).
</p>
<p>
It is guaranteed that target exists in nums.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,4,5], target = 5, start = 3
    Output: 1
    Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

<b>Example 2:</b>

    Input: nums = [1], target = 1, start = 0
    Output: 0
    Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

<b>Example 3:</b>

    Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
    Output: 0
    Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
    
<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 104
- 0 <= start < nums.length
- target is in nums.


<h2>Solution</h2>

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = 2**31-1
        for idx,n in enumerate(nums):
            if n == target:
                min_diff = min(min_diff,abs(idx-start))
        return min_diff
```
