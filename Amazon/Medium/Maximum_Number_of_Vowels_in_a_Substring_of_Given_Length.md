# [Home](./../..)/[Amazon](./..)/[Medium](./)/Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length
<h1>Maximum Number of Vowels in a Substring of Given Length</h1>

<p>
Given a string s and an integer k.
<br>
Return the maximum number of vowel letters in any substring of s with length k.
<br>
Vowel letters in English are (a, e, i, o, u).
</p>

<b>Example 1:</b>

    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
    
<b>Example 2:</b>

    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.
    
<b>Example 3:</b>

    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
    
<b>Example 4:</b>

    Input: s = "rhythms", k = 4
    Output: 0
    Explanation: We can see that s doesn't have any vowel letters.
    
<b>Example 5:</b>
    
    Input: s = "tryhard", k = 4
    Output: 1

<b>Constraints:</b>

- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

<h2>Solution</h2>

```python
# # With extra space
# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         q = deque([])
#         max_len = 0
#         for i in range(k):
#             if s[i] in 'aeiou':
#                 q.append(i)
        
#         for i in range(k,len(s)):
#             max_len = max(max_len,len(q))
            
#             while q and q[0]<=i-k:
#                 q.popleft()
#             if s[i] in 'aeiou':
#                 q.append(i)
            
#         max_len = max(max_len,len(q))
#         return max_len

# Without extra space
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans  = max(cnt, ans)
        return ans    
```
