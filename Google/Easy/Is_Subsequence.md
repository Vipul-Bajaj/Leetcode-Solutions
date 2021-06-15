# [Home](./../..)/[Google](./..)/[Easy](./)/Is_Subsequence
<h1>Is Subsequence</h1>

<p>
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
</p>
<p>
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
</p>

<b>Example 1:</b>

    Input: s = "abc", t = "ahbgdc"
    Output: true
    
<b>Example 2:</b>

    Input: s = "axc", t = "ahbgdc"
    Output: false

<b>Constraint:</b>
- 0 <= s.length <= 100
- 0 <= t.length <= 104
- s and t consist only of lowercase English letters.

<b>Follow up:</b> Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

<h2>Solution</h2>

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        for ch in t:
            if i<n and ch == s[i]:
                i+=1
        if i == n:
            return True
        return False
```
