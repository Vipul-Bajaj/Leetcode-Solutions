# [Home](./../..)/[Apple](./..)/[Easy](./)/Excel_Sheet_Column_Number
<h1>Excel Sheet Column Number</h1>

<p>
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:
</p>

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

<b>Example 1:</b>

    Input: columnTitle = "A"
    Output: 1
    
<b>Example 2:</b>

    Input: columnTitle = "AB"
    Output: 28
    
<b>Example 3:</b>    
    
    Input: columnTitle = "FXSHRXW"
    Output: 2147483647

<b>Constraints:</b>

- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].

<h2>Solution</h2>

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        p = 0
        for i in range(len(columnTitle)-1,-1,-1):
            ch = columnTitle[i]
            res = res + (ord(ch)-ord("A")+1) * (26**p)
            p+=1
        
        return res
```
