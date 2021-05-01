<h1>Reverse Integer</h1>

<p>
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

</p>

<b>Example 1:</b>

    Input: x = 123
    Output: 321
    
<b>Example 2:</b>

    Input: x = -123
    Output: -321
    
<b>Example 3:</b>

    Input: x = 120
    Output: 21

<b>Constraints:</b>

- -2^31 <= x <= 2^31 - 1

<h2>Solution</h2>

```python
class Solution:
    def reverse(self, x: int) -> int:
        min_int = -2**31
        max_int = 2**31-1
        rev = 0
        sign = 1 if x>=0 else -1
        x = abs(x)
        while x!=0:
            pop = x%10
            x//=10
            if rev > max_int//10 or (rev == max_int//10 and pop>7):
                return 0
            rev= rev*10+pop
        
        return rev if sign>0 else -1*rev
```
