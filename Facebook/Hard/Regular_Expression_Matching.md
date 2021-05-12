# [Home](./../..)/[Facebook](./..)/[Hard](./)/Regular_Expression_Matching
<h1>Regular Expression Matching</h1>

<p>
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
</p>

* '.' Matches any single character.
* '*' Matches zero or more of the preceding element.

<p>
The matching should cover the entire input string (not partial).
</p>

<b>Example 1:</b>

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    
<b>Example 2:</b>

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

<b>Example 3:</b>

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

<b>Constraints:</b>

- 0 <= s.length <= 20
- 0 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

<h2>Solution</h2>

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(2,n+1):
            dp[0][i] = dp[0][i-2] if p[i-1] == "*" else False
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or s[i-1]==p[j-2]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]
```
