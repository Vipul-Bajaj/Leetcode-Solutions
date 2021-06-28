# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Minimum_Number_of_Steps_to_Make_Two_Strings_Anagram
<h1>Minimum Number of Steps to Make Two Strings Anagram</h1>

<p>
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
</p>
<p>
Return the minimum number of steps to make t an anagram of s.
</p>
<p>
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
</p>

<b>Example 1:</b>

    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
    
<b>Example 2:</b>

    Input: s = "leetcode", t = "practice"
    Output: 5
    Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
    
<b>Example 3:</b>

    Input: s = "anagram", t = "mangaar"
    Output: 0
    Explanation: "anagram" and "mangaar" are anagrams. 

<b>Constraints:</b>

- 1 <= s.length <= 50000
- s.length == t.length
- s and t contain lower-case English letters only.

<h2>Solution</h2>

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # sc = Counter(s)
        # tc = Counter(t)
        # return sum((sc-tc).values())
        return sum(abs(s.count(i)-t.count(i))for i in "abcdefghijklmnopqrstuvwxyz")//2
```
