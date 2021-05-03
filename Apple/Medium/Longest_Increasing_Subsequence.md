# [Home](./../..)/[Apple](./..)/[Medium](./)/Longest_Increasing_Subsequence
<h1>Longest Increasing Subsequence</h1>

<p>
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

</p>

<b>Example 1:</b>

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    
<b>Example 2:</b>

    Input: nums = [0,1,0,3,2,3]
    Output: 4
    
<b>Example 3:</b>

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

<b>Constraints:</b>

- 1 <= nums.length <= 2500
- -104 <= nums[i] <= 104

<b>Follow up:</b>

- Could you come up with the O(n2) solution?
- Could you improve it to O(n log(n)) time complexity?

<h2>Solution</h2>

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and lis[i]<lis[j]+1:
                    lis[i] = lis[j]+1
        
        return max(lis)
```
