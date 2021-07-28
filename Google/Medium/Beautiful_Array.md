# [Home](./../..)/[Google](./..)/[Medium](./)/Beautiful_Array
<h1>Beautiful Array</h1>

<p>
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:
</p>
<p>
For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].
</p>
<p>
Given n, return any beautiful array nums.  (It is guaranteed that one exists.)
</p>

<b>Example 1:</b>

    Input: n = 4
    Output: [2,1,4,3]
    
<b>Example 2:</b>    

    Input: n = 5
    Output: [3,1,2,5,4]
    
<b>Constraints:</b>

- 1 <= n <= 1000

<h2>Solution</h2>

```python
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= n]
```
