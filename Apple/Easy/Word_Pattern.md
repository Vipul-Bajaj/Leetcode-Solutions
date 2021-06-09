# [Home](./../..)/[Apple](./..)/[Easy](./)/Word_Pattern
<h1>Word Pattern</h1>

<p>
Given a pattern and a string s, find if s follows the same pattern.
</p>
<p>
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
</p>

<b>Example 1:</b>

    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    
<b>Example 2:</b>

    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    
<b>Example 3:</b>

    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
    
<b>Example 4:</b>

    Input: pattern = "abba", s = "dog dog dog dog"
    Output: false

<b>Constraints:</b>

- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lower-case English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

<h2>Solution</h2>

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s = s.split()
        if len(p)!=len(s):
            return False
        hash_map = dict()
        for x,y in zip(p,s):
            if hash_map.setdefault(x,y)!=y:
                return False
        if len(set(hash_map.keys())) != len(set(hash_map.values())):
            return False
        return True
```
