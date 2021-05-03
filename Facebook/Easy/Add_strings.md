# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Add_strings
<h1>Add strings</h1>

<p>
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

</p>

<b>Example 1:</b>

    Input: num1 = "11", num2 = "123"
    Output: "134"
    
<b>Example 2:</b>

    Input: num1 = "456", num2 = "77"
    Output: "533"
    
<b>Example 3:</b>

    Input: num1 = "0", num2 = "0"
    Output: "0"

<b>Constraints:</b>

- 1 <= num1.length, num2.length <= 104
- num1 and num2 consist of only digits.
- num1 and num2 don't have any leading zeros except for the zero itself.

<h2>Solution</h2>

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        n1 = len(num1)
        n2 = len(num2)
        
        i,j = n1-1,n2-1
        while i>=0 or j>=0:
            x1 = ord(num1[i])-ord('0') if i>=0 else 0
            x2 = ord(num2[j])-ord('0') if j>=0 else 0
            res += chr((x1+x2+carry)%10 + ord('0'))
            carry = (x1+x2+carry)//10
            i-=1
            j-=1
        
        if carry:
            res += chr(carry + ord('0'))
            
        return res[::-1]
```
