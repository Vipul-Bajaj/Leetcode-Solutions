# [Home](./../..)/[Facebook](./..)/[Easy](./)/Add_Binary
<h1>Add Binary</h1>

<p>
Given two binary strings a and b, return their sum as a binary string.

</p>

<b>Example 1:</b>

    Input: a = "11", b = "1"
    Output: "100"
    
<b>Example 2:</b>

    Input: a = "1010", b = "1011"
    Output: "10101"

<b>Constraints:</b>

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

<h2>Solution</h2>

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)
```
