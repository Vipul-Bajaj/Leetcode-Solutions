# [Home](./../..)/[Facebook](./..)/[Easy](./)/Valid_Perfect_Square
<h1>Valid Perfect Square</h1>

<p>
Given a positive integer num, write a function which returns True if num is a perfect square else False.
<br>
Follow up: Do not use any built-in library function such as sqrt.
</p>

<b>Example 1:</b>

    Input: num = 16
    Output: true

<b>Example 2:</b>

    Input: num = 14
    Output: false

<b>Constraints:</b>

- 1 <= num <= 2^31 - 1

<h2>Solution</h2>

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 0
        r = num//2
        while l<=r:
            mid = (l+r)//2
            if mid*mid == num:
                return True
            elif mid*mid>num:
                r = mid-1
            else:
                l = mid+1
        return False
```
