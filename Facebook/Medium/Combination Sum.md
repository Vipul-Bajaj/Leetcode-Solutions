<h1>Combination Sum</h1>

<p>
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

<b>Example 1:</b>

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
    
<b>Example 2:</b>

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
    
<b>Example 3:</b>

    Input: candidates = [2], target = 1
    Output: []

<b>Constraints:</b>

- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- All elements of candidates are distinct.
- 1 <= target <= 500

<h2>Solution</h2>

```python
class Solution:
    def combinations(self,candidates,target,arr,s):
        if len(candidates)<=0 or s>target:
            return
        if s == target:
            self.res.append(arr)
            return
        for idx,i in enumerate(candidates):
            if s+i<=target:
                self.combinations(candidates[idx:],target,arr + [i], s+i)
            else:
                break
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.combinations(candidates,target,[],0)
        return self.res
```
