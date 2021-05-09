# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Shortest_Word_Distance_III
<h1>Shortest Word Distance III</h1>

<p>
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.
</p>

<b>Example 1:</b>

    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
    Output: 1

<b>Example 2:</b>
  
    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
    Output: 3
    
<b>Constraints:</b>

- 1 <= wordsDict.length <= 3 * 104
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.

<h2>Solution</h2>

```python
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        self.hash_map = defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.hash_map[word].append(i)
        if word1 == word2:
            word1_ind = self.hash_map[word1]
            i = 0
            j = 1
            min_diff = word1_ind[j]-word1_ind[i]
            while j<len(word1_ind):
                min_diff = min(min_diff,word1_ind[j]-word1_ind[i])
                i+=1
                j+=1
            return min_diff

        word1_ind = self.hash_map[word1]
        word2_ind = self.hash_map[word2]
        min_dist = 2**31
        i=0
        j=0
        while i<len(word1_ind) and j<len(word2_ind):
            min_dist = min(min_dist,abs(word1_ind[i]-word2_ind[j]))
            if word1_ind[i]<word2_ind[j]:
                i+=1
            else:
                j+=1
        return min_dist
```
