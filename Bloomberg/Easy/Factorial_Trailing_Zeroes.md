# [Home](./../..)/[Bloomberg](./..)/[Easy](./)/Factorial_Trailing_Zeroes
<h1>Factorial Trailing Zeroes</h1>

<p>
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
</p>

<b>Example 1:</b>

    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
    
<b>Example 2:</b>

    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

<b>Constraints:</b>

- 0 <= n <= 104

<h2>Solution</h2>

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        c= 0
        i = 5
        while n//i>0:
            c+=n//i
            i*=5
        return c
```
