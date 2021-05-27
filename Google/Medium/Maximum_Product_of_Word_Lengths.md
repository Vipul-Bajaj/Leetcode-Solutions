# [Home](./../..)/[Google](./..)/[Medium](./)/Maximum_Product_of_Word_Lengths
<h1>Maximum Product of Word Lengths</h1>

<p>
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
</p>

<b>Example 1:</b>

    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
    
<b>Example 2:</b>

    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".

<b>Example 3:</b>

    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    Explanation: No such pair of words.

<b>Constraints:</b>

- 2 <= words.length <= 1000
- 1 <= words[i].length <= 1000
- words[i] consists only of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_number = lambda ch : ord(ch) - ord('a')
        max_prod = 0
        hash_map = defaultdict(int)
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_number(ch)
            hash_map[bitmask] = max(hash_map[bitmask], len(word))
        for x in hash_map:
            for y in hash_map:
                if x&y ==0:
                    max_prod = max(max_prod, hash_map[x] * hash_map[y])
        return max_prod
```
