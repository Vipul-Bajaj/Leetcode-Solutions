<h1>Permutations</h1>

<p>
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
<b>Example 2:</b>

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

<b>Example 3:</b>

    Input: nums = [1]
    Output: [[1]]

<b>Constraints:</b>

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

<h2>Solution</h2>

```python
class Solution:
    def generate(self,nums,l,r):
        if l == r:
            self.res.append(nums.copy())
        else:
            for i in range(l,r+1):
                nums[l],nums[i] = nums[i],nums[l]
                self.generate(nums,l+1,r)
                nums[i],nums[l] = nums[l],nums[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.generate(nums,0,len(nums)-1)
        return self.res
```
