# [Home](./../..)/[Facebook](./..)/[Easy](./)/Sentence_Similarity
<h1>Sentence Similarity</h1>

<p>
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].
</p>
<p>
Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.
</p>
<p>
Return true if sentence1 and sentence2 are similar, or false if they are not similar.
</p>
<p>
Two sentences are similar if:
</p>

* They have the same length (i.e., the same number of words)
* sentence1[i] and sentence2[i] are similar.

<p>
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
</p>

<b>Example 1:</b>

    Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
    Output: true
    Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
    
<b>Example 2:</b>

    Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
    Output: true
    Explanation: A word is similar to itself.
    
<b>Example 3:</b>

    Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
    Output: false
    Explanation: As they don't have the same length, we return false.
<b>Constraints:</b>

- 1 <= sentence1.length, sentence2.length <= 1000
- 1 <= sentence1[i].length, sentence2[i].length <= 20
- sentence1[i] and sentence2[i] consist of English letters.
- 0 <= similarPairs.length <= 1000
- similarPairs[i].length == 2
- 1 <= xi.length, yi.length <= 20
- xi and yi consist of lower-case and upper-case English letters.
- All the pairs (xi, yi) are distinct.

<h2>Solution</h2>

```python
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        mapping = defaultdict(set)
        for word1, word2 in similarPairs:
            mapping[word1].add(word2)
            mapping[word2].add(word1)
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2:
                if word1 not in mapping or word2 not in mapping[word1]:
                    return False
        
        return True
```
