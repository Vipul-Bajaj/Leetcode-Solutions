<h1>One Edit Distance</h1>

<p>
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

- Insert exactly one character into s to get t.
- Delete exactly one character from s to get t.
- Replace exactly one character of s with a different character to get t.

</p>

<b>Example 1:</b>

    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.
    
<b>Example 2:</b>

    Input: s = "", t = ""
    Output: false
    Explanation: We cannot get t from s by only one step.
    
<b>Example 3:</b>

    Input: s = "a", t = ""
    Output: true

<b>Constraints:</b>

- 0 <= s.length <= 104
- 0 <= t.length <= 104
- s and t consist of lower-case letters, upper-case letters and/or digits.

<h2>Solution</h2>

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        if m > n:
            return self.isOneEditDistance(t,s)
        if abs(m-n) > 1:
            return False
        if m == n and s == t:
            return False
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
                
        return m + 1 == n
```
