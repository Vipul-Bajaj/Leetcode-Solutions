# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Gray_Code
<h1>Gray Code</h1>

<p>
An n-bit gray code sequence is a sequence of 2n integers where:
</p>

- Every integer is in the inclusive range [0, 2n - 1],
- The first integer is 0,
- An integer appears no more than once in the sequence,
- The binary representation of every pair of adjacent integers differs by exactly one bit, and
- The binary representation of the first and last integers differs by exactly one bit.

<p>
Given an integer n, return any valid n-bit gray code sequence.
</p>

<b>Example 1:</b>

    Input: n = 2
    Output: [0,1,3,2]
    Explanation:
    The binary representation of [0,1,3,2] is [00,01,11,10].
    - 00 and 01 differ by one bit
    - 01 and 11 differ by one bit
    - 11 and 10 differ by one bit
    - 10 and 00 differ by one bit
    [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
    - 00 and 10 differ by one bit
    - 10 and 11 differ by one bit
    - 11 and 01 differ by one bit
    - 01 and 00 differ by one bit
    
<b>Example 2:</b>

    Input: n = 1
    Output: [0,1]
    
<b>Constraints:</b>

- 1 <= n <= 16

<h2>Solution</h2>

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        def btog(n):
            return n^(n>>1)
        for i in range(2**n):
            res.append(btog(i))
        return res
```
