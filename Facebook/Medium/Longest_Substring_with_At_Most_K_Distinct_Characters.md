# [Home](./../..)/[Facebook](./..)/[Medium](./)/Longest_Substring_with_At_Most_K_Distinct_Characters
<h1>Longest Substring with At Most K Distinct Characters</h1>

<p>
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
</p>

<b>Example 1:</b>

    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.
    
<b>Example 2:</b>

    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.

<b>Constraints:</b>

- 1 <= s.length <= 5 * 104
- 0 <= k <= 50

<h2>Solution</h2>

```python
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n*k == 0:
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
            
            if len(hash_map) == k+1:
                _, del_idx = hash_map.popitem(last=False)
                l = del_idx+1
            
            max_len = max(max_len,r-l)
        
        return max_len
```
