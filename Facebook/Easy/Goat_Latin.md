# [Home](./../..)/[Facebook](./..)/[Easy](./)/Goat_Latin
<h1>Goat Latin</h1>

<p>
A sentence sentence is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
</p>
<p>
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
</p>
<p>
The rules of Goat Latin are as follows:
</p>

* If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
* If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
* Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

<p>
Return the final sentence representing the conversion from sentence to Goat Latin. 
</p>

<b>Example 1:</b>

    Input: sentence = "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    
<b>Example 2:</b>

    Input: sentence = "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

<b>Constraints:</b>

- sentence contains only uppercase, lowercase and spaces. Exactly one space between each word.
- 1 <= sentence.length <= 150.

<h2>Solution</h2>

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        
        for i,word in enumerate(sentence):
            if sentence[i][0] not in 'AEIOUaeiou':
                sentence[i] = sentence[i][1:] + sentence[i][0]
            sentence[i] = sentence[i] + 'ma' + 'a'*(i+1)
        return " ".join(sentence)
```
