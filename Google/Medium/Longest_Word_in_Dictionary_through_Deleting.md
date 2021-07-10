# [Home](./../..)/[Google](./..)/[Medium](./)/Longest_Word_in_Dictionary_through_Deleting
<h1>Longest Word in Dictionary through Deleting</h1>

<p>
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
</p>

<b>Example 1:</b>

    Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
    Output: "apple"
    
<b>Example 2:</b>    

    Input: s = "abpcplea", dictionary = ["a","b","c"]
    Output: "a"

<b>Constraints:</b>

- 1 <= s.length <= 1000
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 1000
- s and dictionary[i] consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def isSubsequence(self,word,s):
        i = j = 0
        while i<len(word) and j<len(s):
            if word[i] == s[j]:
                i+=1
            j+=1
        return i == len(word)
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        
        for word in dictionary:
            if self.isSubsequence(word,s):
                return word
        return ""
```
