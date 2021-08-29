# [Home](./../..)/[Google](./..)/[Hard](./)/Patching_Array
<h1>Patching Array</h1>

<p>
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
</p>
<p>
Return the minimum number of patches required.
</p>

<b>Example 1:</b>

    Input: nums = [1,3], n = 6
    Output: 1
    Explanation:
    Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
    Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
    Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
    So we only need 1 patch.

<b>Example 2:</b>

    Input: nums = [1,5,10], n = 20
    Output: 2
    Explanation: The two patches can be [2, 4].

<b>Example 3:</b>

    Input: nums = [1,2,2], n = 5
    Output: 0

<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 104
- nums is sorted in ascending order.
- 1 <= n <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        i = 0
        miss = 1
        l = len(nums)
        while miss<=n:
            if i<l and nums[i]<=miss:
                miss+=nums[i]
                i+=1
            else:
                miss += miss
                patch+=1
                
        return patch
```
