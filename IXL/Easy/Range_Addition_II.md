# [Home](./../..)/[IXL](./..)/[Easy](./)/Range_Addition_II
<h1>Range Addition II</h1>

<p>
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
</p>
<p>
Count and return the number of maximum integers in the matrix after performing all the operations.
</p>

<b>Example 1:</b>

    Input: m = 3, n = 3, ops = [[2,2],[3,3]]
    Output: 4
    Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

<b>Example 2:</b>

    Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    Output: 4

<b>Example 3:</b>

    Input: m = 3, n = 3, ops = []
    Output: 9

<b>Constraints:</b>

- 1 <= m, n <= 4 * 104
- 1 <= ops.length <= 104
- ops[i].length == 2
- 1 <= ai <= m
- 1 <= bi <= n

<h2>Solution</h2>

```python
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x,y in ops:
            m = min(x,m)
            n = min(y,n)
        return m*n
```
