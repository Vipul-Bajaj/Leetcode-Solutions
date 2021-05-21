# [Home](./../..)/[WayFair](./..)/[Easy](./)/Longest_Palindrome
<h1>Longest Palindrome</h1>

<p>
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
</p>

<b>Example 1:</b>

    Input: s = "abccccdd"
    Output: 7
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
    
<b>Example 2:</b>

    Input: s = "a"
    Output: 1
    
<b>Example 3:</b>

    Input: s = "bb"
    Output: 2

<b>Constraints:</b>

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

<h2>Solution</h2>

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        max_len = 0
        odd = False
        for i in count.values():
            if i%2==0:
                max_len+=i
                continue
            odd = True
            max_len += i-1
        return max_len + 1 if odd else max_len
```
