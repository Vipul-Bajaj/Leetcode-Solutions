# [Home](./../..)/[Adobe](./..)/[Easy](./)/Number_of_Good_Pairs
<h1>Number of Good Pairs</h1>

<p>
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    
<b>Example 2:</b>

    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.

<b>Constraints:</b>

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

<h2>Solution</h2>

```python
# #  O(n^2)
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         pairs = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     pairs+=1
                    
#         return pairs
# O(n) solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        h = defaultdict(int)
        for num in nums:
            if num in h:
                pairs += h[num]
            h[num]+=1
        return pairs
```
