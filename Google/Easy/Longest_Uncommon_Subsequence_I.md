# [Home](./../..)/[Google](./..)/[Easy](./)/Longest_Uncommon_Subsequence_I
<h1>Longest Uncommon Subsequence I</h1>

<p>
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.
</p>
<p>
An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
</p>
<p>
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
</p>

- For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


<b>Example 1:</b>

    Input: a = "aba", b = "cdc"
    Output: 3
    Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
    Note that "cdc" is also a longest uncommon subsequence.

<b>Example 2:</b>

    Input: a = "aaa", b = "bbb"
    Output: 3
    Explanation: The longest uncommon subsequences are "aaa" and "bbb".

<b>Example 3:</b>

    Input: a = "aaa", b = "aaa"
    Output: -1
    Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.

<b>Constraint:</b>
- 1 <= a.length, b.length <= 100
- a and b consist of lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a),len(b))
```
