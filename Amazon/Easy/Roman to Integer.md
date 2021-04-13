<h1>Roman to Integer</h1>

<p>
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

<b>Example 1:</b>

    Input: s = "III"
    Output: 3
    
<b>Example 2:</b>

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    
<b>Example 3:</b>

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

<b>Constraints:</b>

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

<h2>Solution</h2>

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_n = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        i = 0
        n = len(s)
        while i<n-1:
            if (s[i]=="I" and s[i+1]=="V") or (s[i]=="I" and s[i+1]=="X") or (s[i]=="I" and s[i+1]=="L") or (s[i]=="I" and s[i+1]=="C") or (s[i]=="I" and s[i+1]=="D") or (s[i]=="I" and s[i+1]=="M"):
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            elif (s[i]=="V" and s[i+1]=="X") or (s[i]=="V" and s[i+1]=="L") or (s[i]=="V" and s[i+1]=="C") or (s[i]=="V" and s[i+1]=="D") or (s[i]=="V" and s[i+1]=="M"):
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            elif (s[i]=="X" and s[i+1]=="L") or (s[i]=="X" and s[i+1]=="C") or (s[i]=="X" and s[i+1]=="D") or (s[i]=="X" and s[i+1]=="M"):
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            elif (s[i]=="L" and s[i+1]=="C") or (s[i]=="L" and s[i+1]=="D") or (s[i]=="L" and s[i+1]=="M"):
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            elif (s[i]=="C" and s[i+1]=="D")or (s[i]=="C" and s[i+1]=="M"):
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            elif s[i]=="D" and s[i+1]=="M":
                num += abs(r_to_n[s[i+1]] - r_to_n[s[i]])
                i+=2
            else:
                num += r_to_n[s[i]]
                i+=1
                
        
        if i==n-1:
            num += r_to_n[s[i]]
        
        return num
```
