# [Home](./../..)/[Facebook](./..)/[Medium](./)/Subsets
<h1>Subsets</h1>

<p>
Given an integer array nums of unique elements, return all possible subsets (the power set).
</p>
<p>
The solution set must not contain duplicate subsets. Return the solution in any order.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

<b>Example 2:</b>

    Input: nums = [0]
    Output: [[],[0]]

<b>Constraints:</b>

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

<h2>Solution</h2>

```python
class Solution:
    def generate(self,nums,subset,subsets):
        subsets.append(subset.copy())
        for i in range(len(nums)):
            subset.append(nums[i])
            self.generate(nums[i+1:],subset,subsets)
            del subset[-1]
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.generate(nums,[],subsets)
        return subsets
```
