# [Home](./../..)/[Thomson Reuters](./..)/[Medium](./)/Longest_Substring_Of_All_Vowels_in_Order
<h1>Longest Substring Of All Vowels in Order</h1>

<p>
A string is considered beautiful if it satisfies the following conditions:
</p>

* Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
* The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).

<p>
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
</p>
<p>
Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
</p>
<p>
A substring is a contiguous sequence of characters in a string.
</p>

<b>Example 1:</b>

    Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    Output: 13
    Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
    
<b>Example 2:</b>

    Input: word = "aeeeiiiioooauuuaeiou"
    Output: 5
    Explanation: The longest beautiful substring in word is "aeiou" of length 5.

<b>Example 3:</b>

    Input: word = "a"
    Output: 0
    Explanation: There is no beautiful substring, so return 0.

<b>Constraints:</b>

- 1 <= word.length <= 5 * 105
- word consists of characters 'a', 'e', 'i', 'o', and 'u'.

<h2>Solution</h2>

```python
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        i = 0
        max_len = 0
        while i<n:
            if word[i]!='a':
                i+=1
                continue
            s = set([word[i]])
            j = i+1
            while j<n and word[j]>=word[j-1]:
                s.add(word[j])
                j+=1
                
            if len(s) == 5:
                max_len = max(max_len,j-i)
            i = j
        return max_len
```
