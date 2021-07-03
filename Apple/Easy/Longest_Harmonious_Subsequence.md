# [Home](./../..)/[Apple](./..)/[Easy](./)/Longest_Harmonious_Subsequence
<h1>Longest Harmonious Subsequence</h1>

<p>
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
</p>
<p>
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
</p>
<p>
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
</p>

<b>Example 1:</b>

    Input: nums = [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].
    
<b>Example 2:</b>

    Input: nums = [1,2,3,4]
    Output: 2
    
<b>Example 3:</b>

    Input: nums = [1,1,1,1]
    Output: 0  

<b>Constraints:</b>

- 1 <= nums.length <= 2 * 104
- -109 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        longest = 0
        for k in nums:
            count[k] = count.get(k,0)+1
            if k+1 in count:
                longest = max(longest,count[k]+count[k+1])
            if k-1 in count:
                longest = max(longest,count[k]+count[k-1])
        return longest
```
