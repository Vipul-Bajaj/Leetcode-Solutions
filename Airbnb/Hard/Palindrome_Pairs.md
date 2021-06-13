# [Home](./../..)/[Airbnb](./..)/[Hard](./)/Palindrome_Pairs
<h1>Palindrome Pairs</h1>

<p>
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
</p>

<b>Example 1:</b>

    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

<b>Example 2:</b>

    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]

<b>Example 3:</b>

    Input: words = ["a",""]
    Output: [[0,1],[1,0]]

<b>Constraints:</b>

- 1 <= words.length <= 5000
- 0 <= words[i].length <= 300
- words[i] consists of lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]

            # Build solutions of case #1. This word will be word 1.
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])

            # Build solutions of case #2. This word will be word 2.
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # Build solutions of case #3. This word will be word 1.
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])

        return solutions
```
