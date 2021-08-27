# [Home](./../..)/[Google](./..)/[Medium](./)/Longest_Uncommon_Subsequence_II
<h1>Longest Uncommon Subsequence II</h1>

<p>
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
</p>
<p>
An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
</p>
<p>
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
</p>

- For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

<b>Example 1:</b>

    Input: strs = ["aba","cdc","eae"]
    Output: 3

<b>Example 2:</b>

    Input: strs = ["aaa","aaa","aa"]
    Output: -1
    
<b>Constraints:</b>

- 1 <= strs.length <= 50
- 1 <= strs[i].length <= 10
- strs[i] consists of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def isSubsequence(self,x,y):
        i,j=0,0
        while i<len(y) and j<len(x):
            if x[j] == y[i]:
                j+=1
            i+=1
        return j == len(x)
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x:-len(x))
        n = len(strs)
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if self.isSubsequence(strs[i],strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1
```
