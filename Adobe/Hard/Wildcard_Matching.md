# [Home](./../..)/[Adobe](./..)/[Hard](./)/Wildcard_Matching
<h1>Wildcard Matching</h1>

<p>
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
</p>

- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

<p>
The matching should cover the entire input string (not partial).
</p>

<b>Example 1:</b>

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    
<b>Example 2:</b>

    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

<b>Example 3:</b>

    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    
<b>Example 4:</b>

    Input: s = "adceb", p = "*a*b"
    Output: true
    Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".   

<b>Constraints:</b>

- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.

<h2>Solution</h2>

```python
# # O(m*n) DP approach
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m,n = len(s),len(p)
#         dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
#         dp[0][0] = True
        
#         for i in range(1,n+1):
#             dp[0][i] = dp[0][i-1] if p[i-1] == "*" else False
        
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if s[i-1] == p[j-1] or p[j-1] == '?':
#                     dp[i][j] = dp[i-1][j-1]
#                 if p[j-1] == "*":
#                     dp[i][j] = dp[i-1][j] or dp[i][j-1]
#         return dp[m][n]
# O(m+n) approach    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        i,j = 0,0
        str_ind,ptn_ind = -1,-1
        
        while i<m:
            if j<n and (s[i] == p[j] or p[j] == '?'):
                i+=1
                j+=1
            elif j<n and p[j] == "*":
                str_ind = i
                ptn_ind = j
                j+=1
            elif ptn_ind != -1:
                i = str_ind + 1
                j = ptn_ind + 1
                str_ind += 1
            else:
                return False
        while j<n and p[j]=='*':
            j+=1
        if j == n:
            return True
        return False
```
