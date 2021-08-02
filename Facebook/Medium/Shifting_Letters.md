# [Home](./../..)/[Facebook](./..)/[Medium](./)/Shifting_Letters
<h1>Shifting Letters</h1>

<p>
You are given a string s of lowercase English letters and an integer array shifts of the same length.
</p>
<p>
Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
</p>

- For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

<p>
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
<br>
Return the final string after all such shifts to s are applied.
</p>

<b>Example 1:</b>

    Input: s = "abc", shifts = [3,5,9]
    Output: "rpl"
    Explanation: We start with "abc".
    After shifting the first 1 letters of s by 3, we have "dbc".
    After shifting the first 2 letters of s by 5, we have "igc".
    After shifting the first 3 letters of s by 9, we have "rpl", the answer.

<b>Example 2:</b>

    Input: s = "aaa", shifts = [1,2,3]
    Output: "gfd"

<b>Constraints:</b>

- 1 <= s.length <= 105
- s consists of lowercase English letters.
- shifts.length == s.length
- 0 <= shifts[i] <= 109
<h2>Solution</h2>

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = [ord(ch) for ch in s]
        c = 0
        for i in range(len(s)-1,-1,-1):
            c = (c+shifts[i])%26
            s[i]+=c
            if s[i]>122:
                s[i]=s[i]-122+96
        s = [chr(ch) for ch in s]
        return "".join(s)
```
