# [Home](./../..)/[Amazon](./..)/[Medium](./)/Longest_Repeating_Character_Replacement
<h1>Longest Repeating Character Replacement</h1>

<p>
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
</p>
<p>
Return the length of the longest substring containing the same letter you can get after performing the above operations.
</p>

<b>Example 1:</b>

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
    
<b>Example 2:</b>

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

<b>Constraints:</b>

- 1 <= s.length <= 105
- s consists of only uppercase English letters.
- 0 <= k <= s.length

<h2>Solution</h2>

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i
```
