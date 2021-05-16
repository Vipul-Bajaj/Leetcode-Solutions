# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/ZigZag_Conversion
<h1>ZigZag Conversion</h1>

<p>
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
</p>

    P   A   H   N
    A P L S I I G
    Y   I   R
    
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

<b>Example 1:</b>

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    
<b>Example 2:</b>

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

<b>Constraints:</b>

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

<h2>Solution</h2>

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""]*numRows
        r = 0
        inc = True
        for ch in s:
            rows[r]+=(ch)
            if inc:
                r+=1
            else:
                r-=1
            if r >= numRows:
                r = max(0,r-2)
                inc = False
            elif r < 0:
                r = min(numRows-1,r+2)
                inc = True
        
        return "".join(rows)
```
