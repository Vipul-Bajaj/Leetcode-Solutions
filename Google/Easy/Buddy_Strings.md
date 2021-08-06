# [Home](./../..)/[Google](./..)/[Easy](./)/Buddy_Strings
<h1>Buddy Strings</h1>

<p>
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
</p>
<p>
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
</p>

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

<b>Example 1:</b>

    Input: s = "ab", goal = "ba"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

<b>Example 2:</b>

    Input: s = "ab", goal = "ab"
    Output: false
    Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

<b>Example 3:</b>

    Input: s = "aa", goal = "aa"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

<b>Example 4:</b>

    Input: s = "aaaaaaabc", goal = "aaaaaaacb"
    Output: true

<b>Constraint:</b>
- 1 <= s.length, goal.length <= 2 * 104
- s and goal consist of lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        i = 0
        m,n = len(s),len(goal)
        if m!=n:
            return False
        a,b = None,None
        while i<m:
            if s[i]!=goal[i]:
                if a is None:
                    a = i
                else:
                    b = i
            i+=1
        if a is not None and b is not None:
            new_s = s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]
            return new_s == goal
        elif a is None and b is None:
             for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if s.count(ch)>=2:
                        return True
        return False
```
