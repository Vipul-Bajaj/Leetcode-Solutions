# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Longest_Substring_Without_Repeating_Characters
<h1>Longest Substring Without Repeating Characters</h1>

<p>
Given a string s, find the length of the longest substring without repeating characters.

</p>

<b>Example 1:</b>

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    
<b>Example 2:</b>

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    
<b>Example 3:</b>

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

<b>Constraints:</b>

- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

<h2>Solution</h2>

```python
# # O(n^2) Approach
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         max_len = 0
#         for i in range(n):
#             visited = set()
#             visited.add(s[i])
#             for j in range(i+1,n):
#                 if s[j] in visited:
#                     break
#                 else:
#                     visited.add(s[j])
#             max_len = max(max_len,len(visited))
#         return max_len
# O(n) Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ch_map = defaultdict(int)
        i = 0
        max_len = 0
        for j in range(n):
            if s[j] in ch_map:
                i = max(ch_map[s[j]],i)
            max_len = max(max_len, j-i+1)
            ch_map[s[j]] = j+1
        return max_len
```
