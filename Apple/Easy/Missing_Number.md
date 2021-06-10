# [Home](./../..)/[Apple](./..)/[Easy](./)/Missing_Number
<h1>Missing Number</h1>

<p>
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
</p>
<p>
<b>Follow up:</b> Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
</p>

<b>Example 1:</b>

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
    
<b>Example 2:</b>

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

<b>Example 3:</b>

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 104
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

<h2>Solution</h2>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#          XOR approach
        all_xor = reduce(lambda x,y:x^y,list(range(0,len(nums)+1)))
        nums_xor = reduce(lambda x,y:x^y,nums)
        return all_xor^nums_xor
#          Summation approach
#         n = len(nums)
#         sum_n = ((n)*(n+1))//2
#         x = sum_n - sum(nums)
#         return x
```
