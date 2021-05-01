<h1>Subarray Sum Equals K</h1>

<p>
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

<b>Example 1:</b>

    Input: nums = [1,1,1], k = 2
    Output: 2
    
<b>Example 2:</b>

    Input: nums = [1,2,3], k = 3
    Output: 2

<b>Constraints:</b>

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

<h2>Solution</h2>

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash_map = defaultdict(int)
        c = 0
        hash_map[0] = 1
        s = 0
        for i in range(n):
            s+=nums[i]
            c+=hash_map[s-k]
            hash_map[s]+=1
        return c
```
