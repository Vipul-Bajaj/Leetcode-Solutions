# [Home](./../..)/[Amazon](./..)/[Easy](./)/Armstrong_Number
<h1>Armstrong Number</h1>

<p>
Given an integer n, return true if and only if it is an Armstrong number.
<br>
The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
</p>

<b>Example 1:</b>

    Input: n = 153
    Output: true
    Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
    
<b>Example 2:</b>

    Input: n = 123
    Output: false
    Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.

<b>Constraints:</b>

- 1 <= n <= 10^8

<h2>Solution</h2>

```python
class Solution:
    def isArmstrong(self, n: int) -> bool:
        digit = len(str(n))
        num = n
        s = 0
        while n>0:
            r = n%10
            n//=10
            s+=r**digit
        return s == num
```
