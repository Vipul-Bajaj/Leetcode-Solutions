# [Home](./../..)/[Spotify](./..)/[Easy](./)/Ransom_Note
<h1>Ransom Note</h1>

<p>
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
</p>
<p>
Each letter in magazine can only be used once in ransomNote.
</p>

<b>Example 1:</b>

    Input: ransomNote = "a", magazine = "b"
    Output: false
    
<b>Example 2:</b>

    Input: ransomNote = "aa", magazine = "ab"
    Output: false

<b>Example 3:</b>

    Input: ransomNote = "aa", magazine = "aab"
    Output: true

<b>Constraints:</b>

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch]<=0:
                return False
            count[ch]-=1
        return True
```
