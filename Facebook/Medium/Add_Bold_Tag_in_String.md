# [Home](./../..)/[Facebook](./..)/[Medium](./)/Add_Bold_Tag_in_String
<h1>Add Bold Tag in String</h1>

<p>
You are given a string s and an array of strings words. You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.
</p>
<p>
Return s after adding the bold tags.
</p>

<b>Example 1:</b>

    Input: s = "abcxyz123", words = ["abc","123"]
    Output: "<b>abc</b>xyz<b>123</b>"

<b>Example 2:</b>

    Input: s = "aaabbcc", words = ["aaa","aab","bc"]
    Output: "<b>aaabbc</b>c"

<b>Constraints:</b>

- 1 <= s.length <= 1000
- 0 <= words.length <= 100
- 1 <= words[i].length <= 1000
- s and words[i] consist of English letters and digits.
- All the values of words are unique.

<h2>Solution</h2>

```python
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        status = [False]*len(s)
        final = []
        for word in words:
            start = s.find(word)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        i = 0
        while i < len(s):
            if status[i]:
                final += ["<b>"]
                while i < len(s) and status[i]:
                    final += [s[i]]
                    i += 1
                final += ["</b>"]
            else:
                final += [s[i]]
                i += 1
        return "".join(final)
```
