# [Home](./../..)/[Two Sigma](./..)/[Medium](./)/Power_of_Four
<h1>Power of Four</h1>

<p>
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
</p>

<b>Example 1:</b>

    Input: n = 16
    Output: true
    
<b>Example 2:</b>

    Input: n = 5
    Output: false

<b>Constraints:</b>

- -231 <= n <= 231 - 1

<h2>Solution</h2>

```python
from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
         return n>0 and (log(n)/log(4))%1==0
```
