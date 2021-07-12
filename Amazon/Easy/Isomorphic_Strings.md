# [Home](./../..)/[Amazon](./..)/[Easy](./)/Isomorphic_Strings
<h1>Isomorphic Strings</h1>

<p>
Given two strings s and t, determine if they are isomorphic.
</p>
<p>
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
</p>
<p>
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
</p>

<b>Example 1:</b>

    Input: s = "egg", t = "add"
    Output: true

<b>Example 2:</b>

    Input: s = "foo", t = "bar"
    Output: false

<b>Example 3:</b>

    Input: s = "paper", t = "title"
    Output: true

<b>Constraints:</b>

- 1 <= s.length <= 5 * 104
- t.length == s.length
- s and t consist of any valid ascii character.

<h2>Solution</h2>

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        for ch_s,ch_t in zip(s,t):
            if hm.setdefault(ch_s,ch_t) != ch_t:
                return False
        return len(hm.values()) == len(set(hm.values()))
```
