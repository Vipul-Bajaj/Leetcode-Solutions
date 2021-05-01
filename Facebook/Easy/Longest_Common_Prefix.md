<h1>Longest Common Prefix</h1>

<p>
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

<b>Example 1:</b>

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    
<b>Example 2:</b>

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

<b>Constraints:</b>

- 0 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort(key=lambda x:len(x))
        n = len(strs)
        if n == 1:
            return strs[0]
        m = len(strs[0])
        if m == 0:
            return ""
        prefix = ""
        for i in range(m):
            flag = True
            for j in range(1,n):
                if strs[0][i] != strs[j][i]:
                    flag = False
                if not flag:
                    break
            if flag == False:
                break
            prefix+=strs[0][i]
        return prefix
```
