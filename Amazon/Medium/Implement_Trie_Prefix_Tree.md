# [Home](./../..)/[Amazon](./..)/[Medium](./)/Implement_Trie_Prefix_Tree
<h1>Implement Trie (Prefix Tree)</h1>

<p>
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
</p>

* Trie() Initializes the trie object.
* void insert(String word) Inserts the string word into the trie.
* boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
</p>

<b>Example 1:</b>

    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

<b>Constraints:</b>

- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 104 calls in total will be made to insert, search, and startsWith.

<h2>Solution</h2>

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['$'] = True
        
    def _search(self,word):    
        curr = self.trie
        for ch in word:
            if ch not in curr:
                return {}
            curr = curr[ch]
        return curr
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return '$' in self._search(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        def prefixSearch(prefix,curr):
            if '$' in curr:
                return True
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in curr:
                    return prefixSearch(prefix+[ch],curr[ch])
            return False
        curr = self._search(prefix)
        return prefixSearch(list(prefix),curr)
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
