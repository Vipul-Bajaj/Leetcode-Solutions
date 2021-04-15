<h1>Fibonacci Number</h1>

<p>
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1<br>
F(n) = F(n - 1) + F(n - 2), for n > 1.<br>
Given n, calculate F(n).

<b>Example 1:</b>

    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    
<b>Example 2:</b>

    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    
<b>Example 3:</b>

    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

<b>Constraints:</b>

- 0 <= n <= 30

<h2>Solution</h2>

```python
class Solution:
    def fib(self, n: int) -> int:
        f = 0
        s = 1
        if n == 0:
            return f
        if n == 1:
            return s
        i = 2
        while i<=n:
            t = f+s
            f = s
            s = t
            i+=1
        return t
```
