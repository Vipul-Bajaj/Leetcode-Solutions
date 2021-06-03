# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Find_the_Longest_Substring_Containing_Vowels_in_Even_Counts
<h1>Find the Longest Substring Containing Vowels in Even Counts</h1>

<p>
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
</p>

<b>Example 1:</b>
  
    Input: s = "eleetminicoworoep"
    Output: 13
    Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
    
<b>Example 2:</b>

    Input: s = "leetcodeisgreat"
    Output: 5
    Explanation: The longest substring is "leetc" which contains two e's.
    
<b>Example 3:</b>

    Input: s = "bcbcbc"
    Output: 6
    Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

<b>Constraints:</b>

- 1 <= s.length <= 5 x 10^5
- s contains only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = {0:0}
        tmp = {'a':0,'e':1,'i':2,'o':3,'u':4}
        cur, ans = 0,0
        for i, c in enumerate(s, 1):
            if c in tmp:
                cur ^= 1 << tmp[c]
            if cur in memo:
                ans = max(ans, i - memo[cur])
            else:
                memo[cur] = i
        return ans
```
