# [Home](./../..)/[Amazon](./..)/[Medium](./)/Reorganize_String
<h1>Reorganize String</h1>

<p>
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
</p>

<b>Example 1:</b>

    Input: S = "aab"
    Output: "aba"
    
<b>Example 2:</b>

    Input: S = "aaab"
    Output: ""

<b>Constraints:</b>

- S will consist of lowercase letters and have length in range [1, 500].

<h2>Solution</h2>

```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        count = Counter(S).most_common()
        # count = sorted(count.items(),key=lambda x:(-x[1],x[0]))
        if count[0][1] * 2 - 1 > n:
            return ""
        s = []
        for k,v in count:
            s.extend(k*v)
        s1 = s[:(n+1)//2]
        s2 = s[(n+1)//2:]
        ret = []
        while s1 and s2:
            ret.append(s1.pop(0))
            ret.append(s2.pop(0))
        if s1:
            ret += s1
        if s2:
            ret += s2
        return "".join(ret)
```
