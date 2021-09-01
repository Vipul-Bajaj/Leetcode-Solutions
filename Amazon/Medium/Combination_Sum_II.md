# [Home](./../..)/[Amazon](./..)/[Medium](./)/Combination_Sum_II
<h1>Combination Sum II</h1>

<p>
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
</p>
<p>
Each number in candidates may only be used once in the combination.
</p>
<p>
Note: The solution set must not contain duplicate combinations.
</p>

<b>Example 1:</b>

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

<b>Example 2:</b>

    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]
    
<b>Constraints:</b>

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

<h2>Solution</h2>

```python
class Solution:
    def combinations(self,candidates,target,arr,s):
        if target<0:
            return
        if 0 == target:
            self.res.append(arr.copy())
            return
        for i in range(s, len(candidates)):
            if i>s and candidates[i] == candidates[i-1]:
                continue
            arr.append(candidates[i])
            self.combinations(candidates,target-candidates[i],arr,i+1)
            arr.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.combinations(candidates,target,[],0)
        return self.res
```
