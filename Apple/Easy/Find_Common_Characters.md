# [Home](./../..)/[Apple](./..)/[Easy](./)/Find_Common_Characters
<h1>Find Common Characters</h1>

<p>
Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
</p>

<b>Example 1:</b>

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]
    
<b>Example 2:</b>

    Input: ["cool","lock","cook"]
    Output: ["c","o"]

<b>Constraints:</b>

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        for a in words:
            res &= collections.Counter(a)
        return list(res.elements())
```
