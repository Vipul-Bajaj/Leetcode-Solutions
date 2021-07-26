# [Home](./../..)/[Virtu Financial](./..)/[Medium](./)/Count_Number_of_Homogenous_Substrings
<h1>Count Number of Homogenous Substrings</h1>

<p>
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
</p>
<p>
A string is homogenous if all the characters of the string are the same.
</p>
<p>
A substring is a contiguous sequence of characters within a string.
</p>

<b>Example 1:</b>

    Input: s = "abbcccaa"
    Output: 13
    Explanation: The homogenous substrings are listed as below:
    "a"   appears 3 times.
    "aa"  appears 1 time.
    "b"   appears 2 times.
    "bb"  appears 1 time.
    "c"   appears 3 times.
    "cc"  appears 2 times.
    "ccc" appears 1 time.
    3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

<b>Example 2:</b>

    Input: s = "xy"
    Output: 2
    Explanation: The homogenous substrings are "x" and "y".

<b>Example 3:</b>

    Input: s = "zzzzz"
    Output: 15  

<b>Constraints:</b>

- 1 <= s.length <= 105
- s consists of lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        ch  = s[0]
        c = 0
        tc = 0
        mod = (10**9)+7
        for i in range(len(s)):
            if s[i] == ch:
                c+=1
            else:
                c = 1
                ch = s[i]
            tc+=c
        return tc%mod
```
