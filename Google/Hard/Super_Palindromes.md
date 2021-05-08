# [Home](./../..)/[Google](./..)/[Hard](./)/Super_Palindromes
<h1>Super Palindromes</h1>

<p>
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].
</p>

<b>Example 1:</b>

    Input: left = "4", right = "1000"
    Output: 4
    Explanation: 4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
    
<b>Example 2:</b>

    Input: left = "1", right = "2"
    Output: 1

<b>Constraints:</b>

- 1 <= left.length, right.length <= 18
- left and right consist of only digits.
- left and right cannot have leading zeros.
- left and right represent integers in the range [1, 1018].
- left is less than or equal to right.

<h2>Solution</h2>

```python
class Solution:
    def checkPalindrome(self,num):
        n = num
        rev = 0
        while n:
            r = n%10
            rev= 10*rev + r
            n//=10
        if rev == num:
            return True
        return False
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        magic = 100000
        
        c= 0
        for i in range(magic):
            s = str(i) 
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v>right:
                break
            if v>=left and self.checkPalindrome(v):
                c+=1
        for i in range(magic):
            s = str(i) 
            t = s + s[::-1]
            v = int(t) ** 2
            if v>right:
                break
            if v>=left and self.checkPalindrome(v):
                c+=1
        return c
```
