# [Home](./../..)/[Apple](./..)/[Easy](./)/Power_of_Two
<h1>Power of Two</h1>

<p>
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
</p>

<b>Example 1:</b>

    Input: n = 1
    Output: true
    Explanation: 20 = 1
    
<b>Example 2:</b>

    Input: n = 16
    Output: true
    Explanation: 24 = 16

<b>Constraints:</b>

- -231 <= n <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and 2**30%n==0
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         if n == 0:
#             return False
#         return n & (n - 1) == 0
```
