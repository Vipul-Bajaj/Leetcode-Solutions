# [Home](./../../..)/[Two Sigma](./../..)/[Medium](./..)/Longest_String_Chain
# [Home](./../../..)/[Two Sigma](./../..)/[Medium](./..)/Longest_String_Chain
<h1>Longest String Chain</h1>

<p>
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

</p>

<b>Example 1:</b>

    Input: words = ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: One of the longest word chain is "a","ba","bda","bdca".
    
<b>Example 2:</b>

    Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    Output: 5

<b>Constraints:</b>

- 1 <= words.length <= 1000
- 1 <= words[i].length <= 16
- words[i] only consists of English lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 1
        words.sort(key = lambda x:len(x))
        hash_map = dict()
        for word in words:
            curr_len = 1
            for i in range(len(word)):
                word_del = word[:i] + word[i+1:]
                prev_len = hash_map.get(word_del,0)
                curr_len = max(curr_len,prev_len+1)
            hash_map[word] = curr_len
            ans = max(ans,curr_len)
        
        return ans
```
