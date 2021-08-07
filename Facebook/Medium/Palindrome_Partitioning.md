# [Home](./../..)/[Facebook](./..)/[Medium](./)/Palindrome_Partitioning
<h1>Palindrome Partitioning</h1>

<p>
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
</p>
<p>
A palindrome string is a string that reads the same backward as forward.
</p>

<b>Example 1:</b>

    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

<b>Example 2:</b>

    Input: s = "a"
    Output: [["a"]]
    
<b>Constraints:</b>

- 1 <= s.length <= 16
- s contains only lowercase English letters.
<h2>Solution</h2>

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[False for k in range(length)] for k in range(length)]
        ret = []
        self.dfs(ret, s, 0, [], dp)
        
        return ret
        
        
    def dfs(self, ret, s, start, currentList, dp):
        if start >= len(s):
            ret.append(list(currentList))
        
        for end in range(start, len(s)):
            if s[end] == s[start] and (end - start <= 2 or dp[start+1][end-1]):
                dp[start][end] = True
                currentList.append(s[start:end+1])
                self.dfs(ret, s, end + 1, currentList, dp)
                currentList.pop()
```
