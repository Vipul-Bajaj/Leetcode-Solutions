# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Consecutive_Characters
<h1>Consecutive Characters</h1>

<p>
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
</p>
<p>
Return the power of the string.
</p>

<b>Example 1:</b>

    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.

<b>Example 2:</b>

    Input: s = "abbcccddddeeeeedcba"
    Output: 5
    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

<b>Example 3:</b>

    Input: s = "triplepillooooow"
    Output: 5

<b>Constraints:</b>

- 1 <= s.length <= 500
- s contains only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def maxPower(self, s: str) -> int:
        max_pow = 1
        curr = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curr+=1
            else:
                max_pow = max(max_pow,curr)
                curr = 1
        max_pow = max(max_pow,curr)
        return max_pow
```
