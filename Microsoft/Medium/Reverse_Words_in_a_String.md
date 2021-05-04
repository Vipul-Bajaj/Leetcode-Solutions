# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Reverse_Words_in_a_String
<h1>Reverse Words in a String</h1>

<p>
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
</p>

<b>Example 1:</b>

    Input: s = "the sky is blue"
    Output: "blue is sky the"
    
<b>Example 2:</b>

    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
    
<b>Example 3:</b>

    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

<b>Constraints:</b>

- 1 <= s.length <= 104
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

<h2>Solution</h2>

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = []
        word = []
        for i in s:
            if i == " ":
                if word:
                    new_s = ["".join(word)] + new_s
                word = []
            else:
                word.append(i)
        if word:
            new_s = ["".join(word)] + new_s
        return " ".join(new_s)
```
