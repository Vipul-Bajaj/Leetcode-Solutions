# [Home](./../..)/[Apple](./..)/[Medium](./)/Interleaving_String
<h1>Interleaving String</h1>

<p>
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
</p>
<p>
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
</p>

* s = s1 + s2 + ... + sn
* t = t1 + t2 + ... + tm
* |n - m| <= 1
* The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

<p>
Note: a + b is the concatenation of strings a and b.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg">

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    
<b>Example 2:</b>

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
    
<b>Example 3:</b>

    Input: s1 = "", s2 = "", s3 = ""
    Output: true

<b>Constraints:</b>

- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i,j = 0,0
        m,n,l = len(s1),len(s2),len(s3)
        if m+n != l:
            return False
        dp = [0 for j in range(n+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                val = 0
                if i == 0 and j == 0:
                    val = 1
                elif j == 0:
                    val = dp[j] and s1[i-1]  == s3[i+j-1]
                elif i == 0:
                    val = dp[j-1] and s2[j-1] == s3[i+j-1]
                else:
                    val = (dp[j] and s1[i-1]  == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
                dp[j] = val
        return dp[n]
```
