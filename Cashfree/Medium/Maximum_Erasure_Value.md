# [Home](./../..)/[Cashfree](./..)/[Medium](./)/Maximum_Erasure_Value
<h1>Maximum Erasure Value</h1>

<p>
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
<br>
Return the maximum score you can get by erasing exactly one subarray.
<br>
An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
</p>

<b>Example 1:</b>

    Input: nums = [4,2,4,5,6]
    Output: 17
    Explanation: The optimal subarray here is [2,4,5,6].
    
<b>Example 2:</b>

    Input: nums = [5,2,1,2,5,2,1,2,5]
    Output: 8
    Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

<b>Constraints:</b>

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        max_val = 0
        seen = set()
        curr_sum = 0
        while end<len(nums):
            while nums[end] in seen:
                seen.remove(nums[start])
                curr_sum-=nums[start]
                start+=1
            curr_sum+=nums[end]
            seen.add(nums[end])
            max_val = max(max_val,curr_sum)
            end+=1
        return max_val
```
