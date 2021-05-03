# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Integer_to_Roman
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Integer_to_Roman
<h1>Integer to Roman</h1>

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

Given an integer, convert it to a roman numeral.

</p>

<b>Example 1:</b>

    Input: num = 3
    Output: "III"
    
<b>Example 2:</b>

    Input: num = 4
    Output: "IV"
    
<b>Example 3:</b>

    Input: num = 9
    Output: "IX"

<b>Example 4:</b>

    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.
    
<b>Example 5:</b>

    Input: num = 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

<b>Constraints:</b>

- 1 <= num <= 3999

<h2>Solution</h2>

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1, 4, 5, 9, 10, 40, 50, 90,  
               100, 400, 500, 900, 1000] 
        sym = ["I", "IV", "V", "IX", "X", "XL",  
               "L", "XC", "C", "CD", "D", "CM", "M"] 
        i = 12
        s = ""
        while num: 
            div = num // nums[i] 
            num %= nums[i] 
      
            while div: 
                s += sym[i]
                div -= 1
            i -= 1
        return s
```
