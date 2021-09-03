# [Home](./../..)/[Amazon](./..)/[Medium](./)/Unique_Binary_Search_Trees
<h1>Unique Binary Search Trees</h1>

<p>
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg">

    Input: n = 3
    Output: 5

<b>Example 2:</b>

    Input: n = 1
    Output: 1
    
<b>Constraints:</b>

- 1 <= n <= 19

<h2>Solution</h2>

```python
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
```
