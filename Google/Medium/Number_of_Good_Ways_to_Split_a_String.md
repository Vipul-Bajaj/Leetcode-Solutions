# [Home](./../..)/[Google](./..)/[Medium](./)/Number_of_Good_Ways_to_Split_a_String
<h1>Number of Good Ways to Split a String</h1>

<p>
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.
</p>

<b>Example 1:</b>

    Input: s = "aacaba"
    Output: 2
    Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
    ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
    ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
    ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
    ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
    ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
    
<b>Example 2:</b>

    Input: s = "abcd"
    Output: 1
    Explanation: Split the string as follows ("ab", "cd").
    
<b>Example 3:</b>

    Input: s = "aaaaa"
    Output: 4
    Explanation: All possible splits are good.

<b>Constraints:</b>

- s contains only lowercase English letters.
- 1 <= s.length <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def numSplits(self, s: str) -> int:
        good_splits = 0
        hash_map = set()
        c = 0
        left = [0]*len(s)
        for idx,ch in enumerate(s):
            if ch not in hash_map:
                hash_map.add(ch)
                c+=1
            left[idx] = c
        c = 0
        right = [0]*len(s)
        hash_map = set()
        for i in range(len(s)-1,-1,-1):
            ch = s[i]
            if ch not in hash_map:
                hash_map.add(ch)
                c+=1
            right[i] = c
        for i in range(1,len(s)):
            if left[i-1] == right[i]:
                good_splits += 1
        return good_splits
```
