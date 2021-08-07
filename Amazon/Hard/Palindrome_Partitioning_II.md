# [Home](./../..)/[Amazon](./..)/[Hard](./)/Palindrome_Partitioning_II
<h1>Palindrome Partitioning II</h1>

<p>
Given a string s, partition s such that every substring of the partition is a palindrome.
</p>
<p>
Return the minimum cuts needed for a palindrome partitioning of s.
</p>

<b>Example 1:</b>

    Input: s = "aab"
    Output: 1
    Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

<b>Example 2:</b>

    Input: s = "a"
    Output: 0

<b>Example 3:</b>

    Input: s = "ab"
    Output: 1
<b>Constraints:</b>

- 1 <= s.length <= 2000
- s consists of lower-case English letters only.
<h2>Solution</h2>

```python
class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        cutsdp = [0]*length
        dp = [[False for k in range(length)] for k in range(length)]
        
        for end in range(0, length):
            min_cut = end
            for start in range(0,end+1):
                if s[end] == s[start] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    min_cut = 0 if start == 0 else min(min_cut,cutsdp[start-1]+1)
            cutsdp[end] = min_cut

        return cutsdp[length-1]
```
