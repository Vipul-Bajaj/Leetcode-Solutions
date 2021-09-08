# [Home](./../..)/[Google](./..)/[Easy](./)/License_Key_Formatting
<h1>License Key Formatting</h1>

<p>
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
</p>
<p>
We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
</p>
<p>
Return the reformatted license key.
</p>

<b>Example 1:</b>

    Input: s = "5F3Z-2e-9-w", k = 4
    Output: "5F3Z-2E9W"
    Explanation: The string s has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

<b>Example 2:</b>

    Input: s = "2-5g-3-J", k = 2
    Output: "2-5G-3J"
    Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

<b>Constraint:</b>
- 1 <= s.length <= 105
- s consists of English letters, digits, and dashes '-'.
- 1 <= k <= 104

<h2>Solution</h2>

```python
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        s = s[::-1]
        groups = [s[i:i+k] for i in range(0,len(s),k)]
        
        return '-'.join(groups)[::-1]
```
