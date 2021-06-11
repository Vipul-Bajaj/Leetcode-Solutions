# [Home](./../..)/[Apple](./..)/[Easy](./)/Reverse_Words_in_a_String_III
<h1>Reverse Words in a String III</h1>

<p>
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
</p>

<b>Example 1:</b>

    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    
<b>Example 2:</b>

    Input: s = "God Ding"
    Output: "doG gniD"
    
<b>Constraints:</b>

- 1 <= s.length <= 5 * 104
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.

<h2>Solution</h2>

```python
class Solution:
    def reverse(self,s,start,end):
        while start<end:
            s[start],s[end] = s[end],s[start]
            end-=1
            start+=1
    def reverseWords(self, s: str) -> str:
        i = 0
        s = list(s)
        while i<len(s):
            j = i
            while j<len(s) and s[j]!=' ':
                j+=1
            self.reverse(s,i,j-1)
            j+=1
            i = j
        return "".join(s)
```
