# [Home](./../..)/[Google](./..)/[Medium](./)/Bold_Words_in_String
<h1>Bold Words in String</h1>

<p>
Given an array of keywords words and a string s, make all appearances of all keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.
</p>
<p>
Return s after adding the bold tags. The returned string should use the least number of tags possible, and the tags should form a valid combination.
</p>

<b>Example 1:</b>

    Input: words = ["ab","bc"], s = "aabcd"
    Output: "a<b>abc</b>d"
    Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

<b>Example 2:</b>

    Input: words = ["ab","cb"], s = "aabcd"
    Output: "a<b>ab</b>cd"

<b>Constraints:</b>

- 1 <= s.length <= 500
- 0 <= words.length <= 50
- 1 <= words[i].length <= 10
- s and words[i] consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
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
