# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Substrings_With_Only_1s
<h1>Number of Substrings With Only 1s</h1>

<p>
Given a binary string s (a string consisting only of '0' and '1's).
</p>
<p>
Return the number of substrings with all characters 1's.
</p>
<p>
Since the answer may be too large, return it modulo 10^9 + 7.
</p>

<b>Example 1:</b>

    Input: s = "0110111"
    Output: 9
    Explanation: There are 9 substring in total with only 1's characters.
    "1" -> 5 times.
    "11" -> 3 times.
    "111" -> 1 time.
    
<b>Example 2:</b>    

    Input: s = "101"
    Output: 2
    Explanation: Substring "1" is shown 2 times in s.
    
<b>Example 3:</b>     

    Input: s = "111111"
    Output: 21
    Explanation: Each substring contains only 1's characters.
    
<b>Example 4:</b>       

    Input: s = "000"
    Output: 0

<b>Constraints:</b>

- s[i] == '0' or s[i] == '1'
- 1 <= s.length <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def numSub(self, s: str) -> int:
        ch  = '1'
        c = 0
        tc = 0
        mod = (10**9)+7
        for i in range(len(s)):
            if s[i] == ch:
                c+=1
                tc+=c
            else:
                c = 0
        return tc%mod
```
