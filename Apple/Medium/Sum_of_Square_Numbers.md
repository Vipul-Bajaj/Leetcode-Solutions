# [Home](./../..)/[Apple](./..)/[Medium](./)/Sum_of_Square_Numbers
<h1>Sum of Square Numbers</h1>

<p>
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
</p>

<b>Example 1:</b>

    Input: c = 5
    Output: true
    Explanation: 1 * 1 + 2 * 2 = 5

<b>Example 2:</b>

    Input: c = 3
    Output: false

<b>Example 3:</b>

    Input: c = 4
    Output: true

<b>Example 4:</b>

    Input: c = 2
    Output: true

<b>Example 5:</b>

    Input: c = 1
    Output: true

<b>Constraints:</b>

- 0 <= c <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j = 0,int(c**0.5)
        while i<=j:
            s = (i**2)+(j**2)
            if s == c:
                return True
            elif s > c:
                j-=1
            else:
                i+=1
        return False
```
