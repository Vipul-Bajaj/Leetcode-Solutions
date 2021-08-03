# [Home](./../..)/[Apple](./..)/[Medium](./)/Subsets_II
<h1>Subsets II</h1>

<p>
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
</p>
<p>
The solution set must not contain duplicate subsets. Return the solution in any order.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

<b>Example 2:</b>

    Input: nums = [0]
    Output: [[],[0]]
    
<b>Constraints:</b>

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

<h2>Solution</h2>

```python
class Solution:
    def generate(self,nums,subset,subsets):
        if subset not in subsets:
            subsets.append(subset.copy())
        for i in range(len(nums)):
            subset.append(nums[i])
            self.generate(nums[i+1:],subset,subsets)
            del subset[-1]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.generate(nums,[],subsets)
        return subsets
```
