# [Home](./../..)/[Bloomberg](./..)/[Easy](./)/Length_of_Last_Word
<h1>Length of Last Word</h1>

<p>
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
</p>
<p>
A word is a maximal substring consisting of non-space characters only.
</p>

<b>Example 1:</b>

    Input: s = "Hello World"
    Output: 5
    
<b>Example 2:</b>

    Input: s = " "
    Output: 0

<b>Constraints:</b>

- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.

<h2>Solution</h2>

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1
        res = 0
        while i>=0 and s[i]==' ':
            i-=1
        while i>=0 and s[i]!=' ':
            res+=1
            i-=1
        return res
```
