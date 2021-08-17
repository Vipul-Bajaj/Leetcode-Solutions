# [Home](./../..)/[Quora](./..)/[Easy](./)/Maximum_Number_of_Words_You_Can_Type
<h1>Maximum Number of Words You Can Type</h1>

<p>
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
</p>
<p>
Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
</p>

<b>Example 1:</b>

    Input: text = "hello world", brokenLetters = "ad"
    Output: 1
    Explanation: We cannot type "world" because the 'd' key is broken.

<b>Example 2:</b>

    Input: text = "leet code", brokenLetters = "lt"
    Output: 1
    Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

<b>Example 3:</b>

    Input: text = "leet code", brokenLetters = "e"
    Output: 0
    Explanation: We cannot type either word because the 'e' key is broken.

<b>Constraints:</b>

- 1 <= text.length <= 104
- 0 <= brokenLetters.length <= 26
- text consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- brokenLetters consists of distinct lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        words = text.split(" ")
        count = len(words)
        for word in words:
            if len(brokenLetters.intersection(set(word))) > 0:
                   count-=1
        return count
```
