# [Home](./../..)/[Adobe](./..)/[Easy](./)/Replace_All_Digits_with_Characters
<h1>Replace All Digits with Characters</h1>

<p>
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
</p>
<p>
There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
</p>

- For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
- For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

<p>
Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
</p>

<b>Example 1:</b>

    Input: s = "a1c1e1"
    Output: "abcdef"
    Explanation: The digits are replaced as follows:
    - s[1] -> shift('a',1) = 'b'
    - s[3] -> shift('c',1) = 'd'
    - s[5] -> shift('e',1) = 'f'

<b>Example 2:</b>

    Input: s = "a1b2c3d4e"
    Output: "abbdcfdhe"
    Explanation: The digits are replaced as follows:
    - s[1] -> shift('a',1) = 'b'
    - s[3] -> shift('b',2) = 'd'
    - s[5] -> shift('c',3) = 'f'
    - s[7] -> shift('d',4) = 'h'

<b>Constraints:</b>

- 1 <= s.length <= 100
- s consists only of lowercase English letters and digits.
- shift(s[i-1], s[i]) <= 'z' for all odd indices i.

<h2>Solution</h2>

```python
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        
        for i in range(1,len(s),2):
            s[i] = chr(ord(s[i-1])+int(s[i]))
        
        return "".join(s)
```
