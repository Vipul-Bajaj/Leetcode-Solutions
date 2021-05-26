# [Home](./../..)/[Facebook](./..)/[Medium](./)/Minimum_Window_Substring
<h1>Minimum Window Substring</h1>

<p>
Given two strings s and t of lengths m and n respectively, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
</p>
<p>
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
</p>

<b>Example 1:</b>

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

<b>Example 2:</b>

    Input: s = "a", t = "a"
    Output: "a"

<b>Constraints:</b>

- m == s.length
- n == t.length
- 1 <= m, n <= 105
- s and t consist of English letters.

<h2>Solution</h2>

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        res_len = n+1
        left,right = 0,0
        start = None
        t_count = Counter(t)
        s_count = Counter()
        required = len(t_count)
        got = 0
        while right<n:
            s_count[s[right]]+=1
            
            if s[right] in t and t_count[s[right]] == s_count[s[right]]:
                got+=1
            
            while got == required:
                if right-left+1<res_len:
                    start = left
                    res_len = right-left+1
                s_count[s[left]]-=1
                if s[left] in t and s_count[s[left]]<t_count[s[left]]:
                    got-=1
                left+=1
            right+=1
            
        return s[start:res_len+start] if (res_len != n+1 ) else ""
```
