# [Home](./../..)/[Google](./..)/[Medium](./)/Delete_Operation_for_Two_Strings
<h1>Delete Operation for Two Strings</h1>

<p>
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

</p>

<b>Example 1:</b>

    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
    
<b>Example 2:</b>

    Input: word1 = "leetcode", word2 = "etco"
    Output: 4
    
<b>Constraints:</b>

- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        result = 0
        m,n = len(word1),len(word2)
        lcs = [[0 for j in range(n+1)]for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif word1[i-1] == word2[j-1]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

        return m-lcs[m][n]+n-lcs[m][n]
```
