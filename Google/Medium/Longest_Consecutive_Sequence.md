# [Home](./../..)/[Google](./..)/[Medium](./)/Longest_Consecutive_Sequence
<h1>Longest Consecutive Sequence</h1>

<p>
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
<br>
You must write an algorithm that runs in O(n) time.
</p>

<b>Example 1:</b>

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
  
<b>Example 2:</b>

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

<b>Constraints:</b>

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        
        for num in num_set:
            if num-1 not in num_set:
                curr = num
                curr_streak = 1
                
                while curr + 1 in num_set:
                    curr +=1
                    curr_streak+=1
                max_len = max(max_len,curr_streak)
        
        return max_len
```
