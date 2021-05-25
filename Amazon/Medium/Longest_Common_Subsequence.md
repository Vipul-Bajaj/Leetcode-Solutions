# [Home](./../..)/[Amazon](./..)/[Medium](./)/Longest_Common_Subsequence
<h1>Longest Common Subsequence</h1>

<p>
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
</p>
<p>
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
</p>

For example, "ace" is a subsequence of "abcde".
<p>
A common subsequence of two strings is a subsequence that is common to both strings.
</p>

<b>Example 1:</b>

    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.
    
<b>Example 2:</b>

   Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
    
<b>Example 3:</b>

    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.
    
<b>Constraints:</b>

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

<h2>Solution</h2>

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        lcs = [[0 for j in range(n+1)] for i in range(m+1)]
        
        # lcs[0][0] = 1
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])
        
        return lcs[m][n]
```
