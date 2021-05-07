# [Home](./../..)/[Goldman Sachs](./..)/[Easy](./)/Find_Pivot_Index
<h1>Find Pivot Index</h1>

<p>
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
</p>

<b>Example 1:</b>

    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11
    
<b>Example 2:</b>

    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.
    
<b>Example 3:</b>

    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -1000 <= nums[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        s = sum(nums)
        n = len(nums)
        pivot = -1
        for i in range(n):
            rsum = s-nums[i]-lsum
            if rsum == lsum:
                pivot = i
                break
            lsum+=nums[i]
        return pivot
```
