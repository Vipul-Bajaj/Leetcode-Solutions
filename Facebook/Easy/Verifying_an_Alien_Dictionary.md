<h1>Verifying an Alien Dictionary</h1>

<p>
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

<b>Example 1:</b>

    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
    
<b>Example 2:</b>

    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    
<b>Example 3:</b>

    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

<b>Constraints:</b>

- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def check_seq(self,word1,word2):
        i,j=0,0
        m,n = len(word1),len(word2)
        while i<m and j<n:
            if word1[i] == word2[j]:
                i+=1
                j+=1
            elif self.dict_hash[word1[i]] < self.dict_hash[word2[j]]:
                return True
            else:
                return False
        if i == m and j <=n:
            return True
        else:
            False
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.dict_hash = defaultdict()
        
        for idx,i in enumerate(order):
            self.dict_hash[i] = idx
            
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if not self.check_seq(word1,word2):
                return False
        return True
```
