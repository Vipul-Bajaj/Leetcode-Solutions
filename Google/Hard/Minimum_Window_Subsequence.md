# [Home](./../..)/[Google](./..)/[Hard](./)/Minimum_Window_Subsequence
<h1>Minimum Window Subsequence</h1>

<p>
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.
</p>
<p>
If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
</p>

<b>Example 1:</b>

    Input: s1 = "abcdebdde", s2 = "bde"
    Output: "bcde"
    Explanation: 
    "bcde" is the answer because it occurs before "bdde" which has the same length.
    "deb" is not a smaller window because the elements of s2 in the window must occur in order.

<b>Example 2:</b>

    Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
    Output: ""

<b>Constraints:</b>

- 1 <= s1.length <= 2 * 104
- 1 <= s2.length <= 100
- s1 and s2 consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_idx = s2_idx = 0
        end = -1
        res = ""
        res_len = float("inf")
        while s1_idx<s1_len:
            if s1[s1_idx] == s2[s2_idx]:
                s2_idx+=1
                if s2_idx == s2_len:
                    end = s1_idx+1
                    s2_idx-=1
                    while s2_idx>=0:
                        if s1[s1_idx] == s2[s2_idx]:
                            s2_idx-=1
                        s1_idx-=1
                    s2_idx+=1
                    s1_idx+=1
                    if end-s1_idx<res_len:
                        res_len = end-s1_idx
                        res = s1[s1_idx:end]
            s1_idx+=1
        
        return res
```
