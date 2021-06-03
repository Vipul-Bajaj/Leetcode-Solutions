# [Home](./../..)/[Google](./..)/[Easy](./)/Backspace_String_Compare
<h1>Backspace String Compare</h1>

<p>
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
<br>
Note that after backspacing an empty text, the text will continue empty.
</p>

<b>Example 1:</b>

    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".
    
<b>Example 2:</b>

    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

<b>Example 3:</b>

    Input: s = "a##c", t = "#a#c"
    Output: true
    Explanation: Both s and t become "c".

<b>Constraint:</b>
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

<h2>Solution</h2>

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for ch in s:
            if s1 and ch == '#':
                s1.pop()
            elif ch != '#':
                s1.append(ch)
        for ch in t:
            if s2 and ch == '#':
                s2.pop()
            elif ch != '#':
                s2.append(ch)
        return s1 == s2
```
