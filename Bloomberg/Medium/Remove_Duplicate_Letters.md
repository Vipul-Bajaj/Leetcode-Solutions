# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Remove_Duplicate_Letters
<h1>Remove Duplicate Letters
</h1>

<p>
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
</p>

<b>Example 1:</b>

    Input: s = "bcabc"
    Output: "abc"
    
<b>Example 2:</b>

    Input: s = "cbacdcbc"
    Output: "acdb"
    
<b>Constraints:</b>

- 1 <= s.length <= 1000
- s consists of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        st = []
        visited = set()
        for ch in s:
            count[ch]-=1
            if ch not in visited:
                while st and count[st[-1]]>0 and st[-1]>ch:
                    visited.remove(st.pop())
                visited.add(ch)
                st.append(ch)
        
        return "".join(st)
```
