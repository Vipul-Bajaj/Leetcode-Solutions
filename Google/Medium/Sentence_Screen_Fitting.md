# [Home](./../..)/[Google](./..)/[Medium](./)/Sentence_Screen_Fitting
<h1>Sentence Screen Fitting</h1>

<p>
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.
</p>
<p>
The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.
</p>

<b>Example 1:</b>

    Input: sentence = ["hello","world"], rows = 2, cols = 8
    Output: 1
    Explanation:
    hello---
    world---
    The character '-' signifies an empty space on the screen.

<b>Example 2:</b>

    Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
    Output: 2
    Explanation:
    a-bcd- 
    e-a---
    bcd-e-
    The character '-' signifies an empty space on the screen.

<b>Example 3:</b>

    Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
    Output: 1
    Explanation:
    i-had
    apple
    pie-i
    had--
    The character '-' signifies an empty space on the screen.
    
<b>Constraints:</b>

- 1 <= sentence.length <= 100
- 1 <= sentence[i].length <= 10
- sentence[i] consists of lowercase English letters.
- 1 <= rows, cols <= 2 * 104

<h2>Solution</h2>

```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence)+' '
        start, l = 0,len(s)
        for i in range(rows):
            start+=cols
            while s[start % l]!=' ':
                start-=1
            start+=1
        return start//l
```
