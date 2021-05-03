# [Home](./../..)/[Google](./..)/[Easy](./)/Power_of_Three
<h1>Power of Three</h1>

<p>
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

</p>

<b>Example 1:</b>

    Input: n = 27
    Output: true
    
<b>Example 2:</b>

    Input: n = 0
    Output: false
    
<b>Example 3:</b>

    Input: n = 9
    Output: true

<b>Constraints:</b>

- -231 <= n <= 231 - 1

<h2>Solution</h2>

```python
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n == 0:
#             return False
#         while n % 3 == 0:
#             n /= 3
#         return n == 1
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 1162261467%n==0
```
