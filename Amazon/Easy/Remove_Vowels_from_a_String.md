# [Home](./../..)/[Amazon](./..)/[Easy](./)/Remove_Vowels_from_a_String
<h1>Remove Vowels from a String</h1>

<p>
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
</p>

<b>Example 1:</b>

    Input: s = "leetcodeisacommunityforcoders"
    Output: "ltcdscmmntyfrcdrs"
    
<b>Example 2:</b>

    Input: s = "aeiou"
    Output: ""

<b>Constraints:</b>

- 1 <= s.length <= 1000
- s consists of only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join([c for c in s if c not in 'aeiou'])
```
