# [Home](./../../..)/[Goldman Sachs](./../..)/[Easy](./..)/First_Unique_Character_in_a_String
<h1>First Unique Character in a String</h1>

<p>
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

</p>

<b>Example 1:</b>

    Input: s = "leetcode"
    Output: 0
    
<b>Example 2:</b>

    Input: s = "loveleetcode"
    Output: 2
    
<b>Example 3:</b>

    Input: s = "aabb"
    Output: -1

<b>Constraints:</b>

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = defaultdict(list)
        for idx,ch in enumerate(s):
            hash_map[ch].append(idx)
        
        min_idx = 2**31-1
        for k,v in hash_map.items():
            if len(v) == 1:
                min_idx = min(min_idx,v[0])
        
        return -1 if min_idx == 2**31-1 else min_idx
```
