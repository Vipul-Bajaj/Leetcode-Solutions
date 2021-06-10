# [Home](./../..)/[Facebook](./..)/[Medium](./)/Sum_of_Two_Integers
<h1>Sum of Two Integers</h1>

<p>
Given two integers a and b, return the sum of the two integers without using the operators + and -.
</p>

<b>Example 1:</b>

    Input: a = 1, b = 2
    Output: 3
    
<b>Example 2:</b>

    Input: a = 3, b = 2
    Output: 5

<b>Constraints:</b>

- -1000 <= a, b <= 1000

<h2>Solution</h2>

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x,y = abs(a),abs(b)
        
        if x<y:
            return self.getSum(b,a)
        
        sign = 1 if a>0 else -1
        
        if a*b>=0:
            while y:
                x,y = x^y,(x&y)<<1
        else:
            while y:
                x,y = x^y,((~x)&y)<<1
                
        return x*sign
```
