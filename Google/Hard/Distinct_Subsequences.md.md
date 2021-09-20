# [Home](./../..)/[Google](./..)/[Hard](./)/Distinct_Subsequences
<h1>Distinct Subsequences</h1>

<p>
Given two strings s and t, return the number of distinct subsequences of s which equals t.
</p>
<p>
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
</p>
<p>
It is guaranteed the answer fits on a 32-bit signed integer.
</p>

<b>Example 1:</b>

    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from S.
    rabbbit
    rabbbit
    rabbbit

<b>Example 2:</b>

    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can generate "bag" from S.
    babgbag
    babgbag
    babgbag
    babgbag
    babgbag


<b>Constraints:</b>

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.

<h2>Solution</h2>

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        
        dp = [[0 for j in range(n+1)]for i in range(m+1)]
        
        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = dp[i+1][j]
                
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]
```
