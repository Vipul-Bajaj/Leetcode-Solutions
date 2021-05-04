# [Home](./../..)/[Amazon](./..)/[Easy](./)/Rotate_String
<h1>Rotate String</h1>

<p>
We are given two strings, A and B.<br>

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
</p>

<b>Example 1:</b>

    Input: A = 'abcde', B = 'cdeab'
    Output: true
    
<b>Example 2:</b>

    Input: A = 'abcde', B = 'abced'
    Output: false

<b>Constraints:</b>

- A and B will have length at most 100.

<h2>Solution</h2>

```python
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        a = len(A)
        b = len(B)
        if a!=b:
            return False
        if A == B:
            return True
        A = list(A)
        B = list(B)
        for i in range(1,a):
            new_A = A[i:] + A[:i]
            new_A = A[i:] + A[:i]
            if new_A == B:
                return True
        return False
```
