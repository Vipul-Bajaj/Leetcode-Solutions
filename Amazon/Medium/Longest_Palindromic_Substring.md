<h1>Longest Palindromic Substring</h1>

<p>
Given a string s, return the longest palindromic substring in s.

<b>Example 1:</b>

    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

<b>Example 2:</b>

    Input: s = "cbbd"
    Output: "bb"

<b>Example 3:</b>

    Input: s = "a"
    Output: "a"

<b>Example 4:</b>

    Input: s = "ac"
    Output: "a"
 
<b>Constraints:</b>

- 1 <= s.length <= 1000
- s consist of only digits and English letters (lower-case and/or upper-case)

<h2>Solution</h2>

```python
class Solution:
    def check_at_centre(self,s, left, right):
        l = left
        r= right
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1;
            r+=1;
        return r-l-1
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) <1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.check_at_centre(s,i,i)
            l2 = self.check_at_centre(s,i,i+1)
            l = max(l1,l2)
            
            if l > end-start:
                start = i-(l-1)//2
                end = i+l//2
                
        return s[start:end+1]
```
