# [Home](./../..)/[Google](./..)/[Medium](./)/Repeated_String_Match

<h1>Repeated String Match</h1>

<p>
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
</p>
<p>
Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".
</p>

<b>Example 1:</b>

    Input: a = "abcd", b = "cdabcdab"
    Output: 3
    Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

<b>Example 2:</b>

    Input: a = "a", b = "aa"
    Output: 2

<b>Example 3:</b>

    Input: a = "a", b = "a"
    Output: 1

<b>Example 4:</b>

    Input: a = "abc", b = "wxyz"
    Output: -1
    
<b>Constraints:</b>

- 1 <= a.length <= 104
- 1 <= b.length <= 104
- a and b consist of lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = 0
        og = ""
        while len(og) < len(b):
            og+=a
            n+=1
            if b in og:
                return n
        og+=a
        if b in og:
            return n+1
        
        return -1
```
