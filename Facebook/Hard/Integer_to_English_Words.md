# [Home](./../..)/[Facebook](./..)/[Hard](./)/Integer_to_English_Words
<h1>Integer to English Words</h1>

<p>
Convert a non-negative integer num to its English words representation.
</p>

<b>Example 1:</b>

    Input: num = 123
    Output: "One Hundred Twenty Three"
    
<b>Example 2:</b>

    Input: num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"

<b>Example 3:</b>

    Input: num = 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    
<b>Example 4:</b>

    Input: num = 1234567891
    Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
<b>Constraints:</b>

- 0 <= num <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num%1000) + self.thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)
```
