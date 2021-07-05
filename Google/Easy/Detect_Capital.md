# [Home](./../..)/[Google](./..)/[Easy](./)/Detect_Capital
<h1>Detect Capital</h1>

<p>
We define the usage of capitals in a word to be right when one of the following cases holds:
</p>

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

<p>
Given a string word, return true if the usage of capitals in it is right.
</p>

<b>Example 1:</b>

    Input: word = "USA"
    Output: true
    
<b>Example 2:</b>

    Input: word = "FlaG"
    Output: false

<b>Constraint:</b>

- 1 <= word.length <= 100
- word consists of lowercase and uppercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n == 1:
            return True
        first,second = word[0].isupper(),word[1].isupper()
        
        if first and second:
            for i in range(2,n):
                if not word[i].isupper():
                    return False
        else:
            for i in range(1,n):
                if word[i].isupper():
                    return False
        return True
```
