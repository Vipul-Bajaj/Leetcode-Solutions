# [Home](./../..)/[Amazon](./..)/[Medium](./)/Longest_Substring_with_At_Most_Two_Distinct_Characters
<h1>Longest Substring with At Most Two Distinct Characters</h1>

<p>
Given a string s, return the length of the longest substring that contains at most two distinct characters.
</p>

<b>Example 1:</b>

    Input: s = "eceba"
    Output: 3
    Explanation: The substring is "ece" which its length is 3.
    
<b>Example 2:</b>

    Input: s = "ccaabbb"
    Output: 5
    Explanation: The substring is "aabbb" which its length is 5.

<b>Constraints:</b>

- 1 <= s.length <= 104
- s consists of English letters.

<h2>Solution</h2>

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n*2 == 0:
            return 0
        l,r = 0,0
        hash_map = OrderedDict()
        
        max_len = 1
        while r<n:
            ch = s[r]
            if ch in hash_map:
                del hash_map[ch]
            hash_map[ch] = r
            r+=1
            
            if len(hash_map) == 3:
                _, del_idx = hash_map.popitem(last=False)
                l = del_idx+1
            
            max_len = max(max_len,r-l)
        
        return max_len
```
