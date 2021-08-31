# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Permutations_II
<h1>Permutations_II</h1>

<p>
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
</p>

<b>Example 1:</b>

    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]

<b>Example 2:</b>

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

<b>Constraints:</b>

- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

<h2>Solution</h2>

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False]*len(nums)
        self.backtrack(nums,[],res,used)
        return res
        
    def backtrack(self,nums,temp,res,used):
        if len(temp) == len(nums):
            res.append(temp.copy())
            
        for i in range(len(nums)):
            if used[i] or (i>0 and nums[i] == nums[i-1] and used[i-1]):
                continue
            used[i] = True
            temp.append(nums[i])
            self.backtrack(nums,temp,res,used)
            used[i] = False
            temp.pop()
```
