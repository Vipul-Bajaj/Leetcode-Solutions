# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Matching_Subsequences
<h1>Number of Matching Subsequences</h1>

<p>
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
</p>
<p>
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
</p>

* For example, "ace" is a subsequence of "abcde".

<b>Example 1:</b>

    Input: s = "abcde", words = ["a","bb","acd","ace"]
    Output: 3
    Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
  
<b>Example 2:</b>

    Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    Output: 2
 
<b>Constraints:</b>

* 1 <= s.length <= 5 * 104
* 1 <= words.length <= 5000
* 1 <= words[i].length <= 50
* s and words[i] consist of only lowercase English letters.

<h2>Solution</h2>

```python
class Solution(object):
    def numMatchingSubseq(self, S, words):
#         Iterator apporach
#         ans = 0
#         heads = [[] for _ in range(26)]
#         for word in words:
#             it = iter(word)
#             heads[ord(next(it)) - ord('a')].append(it)

#         for letter in S:
#             letter_index = ord(letter) - ord('a')
#             old_bucket = heads[letter_index]
#             heads[letter_index] = []

#             while old_bucket:
#                 it = old_bucket.pop()
#                 nxt = next(it, None)
#                 if nxt:
#                     heads[ord(nxt) - ord('a')].append(it)
#                 else:
#                     ans += 1

#         return ans
    
#       Dict approach 
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
```
