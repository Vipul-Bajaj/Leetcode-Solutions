<h1>Valid Anagram</h1>

<p>
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
  
<b>Example 1:</b>

    Input: s = "anagram", t = "nagaram"
    Output: true
    
<b>Example 2:</b>

    Input: s = "rat", t = "car"
    Output: false

<b>Constraints:</b>

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = Counter(s)
    
        for i in t:
            if i in count and count[i]>0:
                count[i]-=1
                
        for v in count.values():
            if v!=0:
                return False
        return True
```
