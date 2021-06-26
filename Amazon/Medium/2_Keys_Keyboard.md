# [Home](./../..)/[Amazon](./..)/[Medium](./)/2_Keys_Keyboard
<h1>2 Keys Keyboard</h1>

<p>
There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:
</p>

- Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
- Paste: You can paste the characters which are copied last time.

<p>
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
</p>

<b>Example 1:</b>

    Input: n = 3
    Output: 3
    Explanation: Intitally, we have one character 'A'.
    In step 1, we use Copy All operation.
    In step 2, we use Paste operation to get 'AA'.
    In step 3, we use Paste operation to get 'AAA'.
    
<b>Example 2:</b>

    Input: n = 1
    Output: 0

<b>Constraints:</b>

- 1 <= n <= 1000

<h2>Solution</h2>

```python
class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
```
