# [Home](./../..)/[Dropbox](./..)/[Hard](./)/Number_of_Valid_Words_for_Each_Puzzle
<h1>Number of Valid Words for Each Puzzle</h1>

<p>
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
</p>

* word contains the first letter of puzzle.
* For each letter in word, that letter is in puzzle.
  For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

<p>
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
</p>

<b>Example 1:</b>

    Input: 
    words = ["aaaa","asas","able","ability","actt","actor","access"], 
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    Output: [1,1,3,2,4,0]
    Explanation:
    1 valid word for "aboveyz" : "aaaa" 
    1 valid word for "abrodyz" : "aaaa"
    3 valid words for "abslute" : "aaaa", "asas", "able"
    2 valid words for "absoryz" : "aaaa", "asas"
    4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
    There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

<b>Constraints:</b>

- 1 <= words.length <= 10^5
- 4 <= words[i].length <= 50
- 1 <= puzzles.length <= 10^4
- puzzles[i].length == 7
- words[i][j], puzzles[i][j] are English lowercase letters.
- Each puzzles[i] doesn't contain repeated characters.
 
<h2>Solution</h2>

```python
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         out = []
#         words_set = {}
#         for word in words:
#             words_set[word] = set(word)
#         for puzzle in puzzles:
#             puzzle_set = set(puzzle)
#             word_count = 0
#             for word,word_set in words_set.items():
#                 if puzzle[0] in word and word_set.difference(puzzle_set) == set():
#                     word_count+=1
#             out.append(word_count)
        
#         return out
        res = []
        cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
        for p in puzzles:
            bfs = [p[0]]
            for c in p[1:]:
                bfs += [s + c for s in bfs]
            res.append(sum(cnt[''.join(sorted(s))] for s in bfs))
        return res
```
