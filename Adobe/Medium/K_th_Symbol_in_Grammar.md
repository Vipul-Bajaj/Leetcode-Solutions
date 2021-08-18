# [Home](./../..)/[Adobe](./..)/[Medium](./)/K_th_Symbol_in_Grammar
<h1>K-th Symbol in Grammar</h1>

<p>
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
</p>

- For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

<p>
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
</p>

<b>Example 1:</b>

    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1: 0

<b>Example 2:</b>

    Input: n = 2, k = 1
    Output: 0
    Explanation:
    row 1: 0
    row 2: 01

<b>Example 3:</b>

    Input: n = 2, k = 2
    Output: 1
    Explanation:
    row 1: 0
    row 2: 01

<b>Example 4:</b>

    Input: n = 3, k = 1
    Output: 0
    Explanation:
    row 1: 0
    row 2: 01
    row 3: 0110
    
<b>Constraints:</b>

- 1 <= n <= 30
- 1 <= k <= 2n - 1

<h2>Solution</h2>

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1
```
