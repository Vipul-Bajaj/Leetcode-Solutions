# [Home](./../..)/[Amazon](./..)/[Medium](./)/Vowel_Spellchecker
<h1>Vowel Spellchecker</h1>

<p>
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:
</p>

* Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    * Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    * Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    * Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
* Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    * Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    * Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    * Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
<p>
In addition, the spell checker operates under the following precedence rules:
</p>

* When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
* When the query matches a word up to capitlization, you should return the first such match in the wordlist.
* When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
* If the query has no matches in the wordlist, you should return the empty string.

<p>
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
</p>

<b>Example 1:</b>

    Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    
<b>Example 2:</b>

    Input: wordlist = ["yellow"], queries = ["YellOw"]
    Output: ["yellow"]

<b>Constraints:</b>

- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- wordlist[i] and queries[i] consist only of only English letters.

<h2>Solution</h2>

```python
class Solution:
    def mask_vowels(self,word):
        return "".join(['*' if c in 'aeiou' else c for c in word])
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfect_words = set(wordlist)
        words_cap = {}
        words_vowel = {}
        
        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow,word)
            words_vowel.setdefault(self.mask_vowels(wordlow),word)
        
        out = []
        for query in queries:
            if query in perfect_words:
                out.append(query)
                continue
            query_lower = query.lower()
            if query_lower in words_cap:
                out.append(words_cap[query_lower])
                continue
            query_masked = self.mask_vowels(query_lower)
            if query_masked in words_vowel:
                out.append(words_vowel[query_masked])
                continue
            out.append("")
        return out
```
