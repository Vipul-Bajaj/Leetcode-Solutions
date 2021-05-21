# [Home](./../..)/[Apple](./..)/[Medium](./)/Find_and_Replace_Pattern
<h1>Find and Replace Pattern</h1>

<p>
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
</p>
<p>
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
</p>
<p>
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
</p>

<b>Example 1:</b>

    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
    
<b>Example 2:</b>

    Input: words = ["a","b","c"], pattern = "a"
    Output: ["a","b","c"]

<b>Constraints:</b>

- 1 <= pattern.length <= 20
- 1 <= words.length <= 50
- words[i].length == pattern.length
- pattern and words[i] are lowercase English letters.

<h2>Solution</h2>

```python
# My Solution
# class Solution:
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#         words_list = []
#         out = []
#         distinct_ch_pattern = len(Counter(pattern).keys())
#         for word in words:
#             if len(Counter(word).keys()) == distinct_ch_pattern:
#                 words_list.append(word)
#         pattern_map = {}
#         n = 1
#         pattern_list = []
#         for ch in pattern:
#             if ch not in pattern_map:
#                 pattern_map[ch]=n
#                 n+=1
#             pattern_list.append(pattern_map[ch])
#         for word in words_list:
#             n = 1
#             word_map = {}
#             word_list = []
#             for ch in word:
#                 if ch not in word_map:
#                     word_map[ch]=n
#                     n+=1
#                 word_list.append(word_map[ch])
#             if word_list == pattern_list:
#                 out.append(word)
        
#         return out
# Leetcode solution
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
```
