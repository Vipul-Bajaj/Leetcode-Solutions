# [Home](./../..)/[Facebook](./..)/[Medium](./)/Pow(x,n)
<h1>Pow(x, n)</h1>

<p>
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
</p>

<b>Example 1:</b>

    Input: x = 2.00000, n = 10
    Output: 1024.00000
    
<b>Example 2:</b>

    Input: x = 2.10000, n = 3
    Output: 9.26100
    
<b>Example 3:</b>

    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

<b>Constraints:</b>

- -100.0 < x < 100.0
- -231 <= n <= 231-1
- -104 <= xn <= 104

<h2>Solution</h2>

```python
class Solution:
    def pow(self,x,n):
        if x == 0 or x == 0.0:
            return 0
        if n == 0 or n == 0.0:
            return 1
        ans = self.pow(x,n//2)
        if n%2==0:
            return (ans*ans)
        else:
            return (x*ans*ans)
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        return self.pow(x,n)
```
