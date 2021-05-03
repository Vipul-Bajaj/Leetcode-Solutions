# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Excel_Sheet_Column_Title
<h1>Excel Sheet Column Title</h1>

<p>
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

</p>

<b>Example 1:</b>

    Input: columnNumber = 1
    Output: "A"
    
<b>Example 2:</b>

    Input: columnNumber = 28
    Output: "AB"
    
<b>Example 3:</b>

    Input: columnNumber = 701
    Output: "ZY"

<b>Constraints:</b>

- 1 <= columnNumber <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ""
        while n:
            rem = n%26
            n = n//26
            if rem == 0:
                n-=1
                rem = 26
            res = chr(ord('A')+(rem-1)) + res
        
        return res
```
