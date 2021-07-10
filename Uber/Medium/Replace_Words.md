# [Home](./../..)/[Uber](./..)/[Medium](./)/Replace_Words
<h1>Replace Words</h1>

<p>
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
</p>
<p>
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
</p>
<p>
Return the sentence after the replacement.
</p>

<b>Example 1:</b>
  
    Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
    
<b>Example 2:</b>
  
    Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
    Output: "a a b c"
    
<b>Example 3:</b>

    Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    Output: "a a a a a a a a bbb baba a"
    
<b>Example 4:</b>
    
    Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"

<b>Example 5:</b>

    Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
    Output: "it is ab that this solution is ac"

<b>Constraints:</b>

- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lower-case letters.
- 1 <= sentence.length <= 10^6
- sentence consists of only lower-case letters and spaces.
- The number of words in sentence is in the range [1, 1000]
- The length of each word in sentence is in the range [1, 1000]
- Each two consecutive words in sentence will be separated by exactly one space.
- sentence does not have leading or trailing spaces.

<h2>Solution</h2>

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = self._getNode()
    
    def _getNode(self):
        return TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children.setdefault(ch,TrieNode())
            
        curr.isEnd = True
    
    def search(self,word):
        curr = self.root
        prefix = []
        for ch in word:
            if ch in curr.children:
                prefix.append(ch)
                curr = curr.children[ch]
                if curr.isEnd:
                    return "".join(prefix)
            else:
                return ""
        return ""
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        out = []
        for word in sentence.split(" "):
            searched = trie.search(word)
            if searched=='':
                out.append(word)
            else:
                out.append(searched)
        return " ".join(out)
```
