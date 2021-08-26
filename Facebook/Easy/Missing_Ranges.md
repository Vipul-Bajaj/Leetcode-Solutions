# [Home](./../..)/[Facebook](./..)/[Easy](./)/Missing_Ranges
<h1>Missing Ranges</h1>

<p>
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
</p>
<p>
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
</p>
<p>
Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
</p>
<p>
Each range [a,b] in the list should be output as:
</p>

- "a->b" if a != b
- "a" if a == b

<b>Example 1:</b>

    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: ["2","4->49","51->74","76->99"]
    Explanation: The ranges are:
    [2,2] --> "2"
    [4,49] --> "4->49"
    [51,74] --> "51->74"
    [76,99] --> "76->99"

<b>Example 2:</b>

    Input: nums = [], lower = 1, upper = 1
    Output: ["1"]
    Explanation: The only missing range is [1,1], which becomes "1".

<b>Example 3:</b>

    Input: nums = [], lower = -3, upper = -1
    Output: ["-3->-1"]
    Explanation: The only missing range is [-3,-1], which becomes "-3->-1".

<b>Example 4:</b>

    Input: nums = [-1], lower = -1, upper = -1
    Output: []
    Explanation: There are no missing ranges since there are no missing numbers.

<b>Example 5:</b>

    Input: nums = [-1], lower = -2, upper = -1
    Output: ["-2"]

<b>Constraints:</b>

- -109 <= lower <= upper <= 109
- 0 <= nums.length <= 100
- lower <= nums[i] <= upper
- All the values of nums are unique.

<h2>Solution</h2>

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # formats range in the requested format
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))
            prev = curr
        return result
```
