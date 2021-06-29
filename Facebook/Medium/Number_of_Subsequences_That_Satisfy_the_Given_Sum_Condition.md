# [Home](./../..)/[Facebook](./..)/[Medium](./)/Number_of_Subsequences_That_Satisfy_the_Given_Sum_Condition
<h1>Number of Subsequences That Satisfy the Given Sum Condition</h1>

<p>
Given an array of integers nums and an integer target.
<br>
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
</p>

<b>Example 1:</b>

    Input: nums = [3,5,6,7], target = 9
    Output: 4
    Explanation: There are 4 subsequences that satisfy the condition.
    [3] -> Min value + max value <= target (3 + 3 <= 9)
    [3,5] -> (3 + 5 <= 9)
    [3,5,6] -> (3 + 6 <= 9)
    [3,6] -> (3 + 6 <= 9)
    
<b>Example 2:</b>

    Input: nums = [3,3,6,8], target = 10
    Output: 6
    Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
    [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

<b>Example 3:</b>

    Input: nums = [2,3,3,4,6,7], target = 12
    Output: 61
    Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
    Number of valid subsequences (63 - 2 = 61).

<b>Example 4:</b>

    Input: nums = [5,2,4,1,7,6,8], target = 16
    Output: 127
    Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127

<b>Constraints:</b>

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 106
- 1 <= target <= 106

<h2>Solution</h2>

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        mod = (10**9)+7
        l,r = 0,n-1
        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                count+=pow(2,r-l,mod)
                l+=1
        
        return count%mod
```
