# [Home](./../..)/[Amazon](./..)/[Medium](./)/Find_All_Anagrams_in_a_String
<h1>Find All Anagrams in a String</h1>

<p>
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
</p>

<b>Example 1:</b>

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    
<b>Example 2:</b>

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

<b>Constraints:</b>

- 1 <= s.length, p.length <= 3 * 104
- s and p consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        if m<n:
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        out = []
        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        for i in range(m):
            s_count[ord(s[i])-ord('a')]+=1
            
            if i>=n:
                s_count[ord(s[i-n])-ord('a')]-=1
            if p_count == s_count:
                out.append(i-n+1)
        return out
```
