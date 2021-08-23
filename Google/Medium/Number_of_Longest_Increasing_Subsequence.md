# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Longest_Increasing_Subsequence
<h1>Number of Longest Increasing Subsequence</h1>

<p>
Given an integer array nums, return the number of longest increasing subsequences.
</p>
<p>
Notice that the sequence has to be strictly increasing.
</p>

<b>Example 1:</b>

    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

<b>Example 2:</b>

    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

<b>Constraints:</b>

- 1 <= nums.length <= 2000
- -106 <= nums[i] <= 106

<h2>Solution</h2>

```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [[1,1] for _ in range(n)]
        longest = 1
        for i,num in enumerate(nums):
            max_len,count = 1,0
            for j in range(i):
                if nums[j]<num:
                    if lis[j][0]+1>max_len:
                        max_len = lis[j][0]+1
                        count = 0
                    if lis[j][0] == max_len-1:
                        count+=lis[j][1]
                        
            lis[i] = [max_len,max(count,lis[i][1])]
            longest = max(longest,max_len)
        return sum([item[1] for item in lis if item[0] == longest])
```
