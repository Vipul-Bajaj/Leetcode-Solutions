# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Shortest_Word_Distance_II
<h1>Shortest Word Distance II</h1>

<p>
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

* WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
* int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
</p>

<b>Example 1:</b>

    Input
    ["WordDistance", "shortest", "shortest"]
    [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    Output
    [null, 3, 1]

    Explanation
    WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
    wordDistance.shortest("coding", "practice"); // return 3
    wordDistance.shortest("makes", "coding");    // return 1

<b>Constraints:</b>

- 1 <= wordsDict.length <= 3 * 104
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.
- word1 != word2
- At most 5000 calls will be made to shortest.

<h2>Solution</h2>

```python
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hash_map = defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.hash_map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
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

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
```
