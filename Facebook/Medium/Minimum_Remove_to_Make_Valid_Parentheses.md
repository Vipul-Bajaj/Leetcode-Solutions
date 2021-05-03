# [Home](./../..)/[Facebook](./..)/[Medium](./)/Minimum_Remove_to_Make_Valid_Parentheses
<h1>Minimum Remove to Make Valid Parentheses</h1>

<p>
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

</p>

<b>Example 1:</b>

    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
    
<b>Example 2:</b>

    Input: s = "a)b(c)d"
    Output: "ab(c)d"
    
<b>Example 3:</b>

    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.
    
<b>Example 4:</b>

    Input: s = "(a(b(c)d)"
    Output: "a(b(c)d)"

<b>Constraints:</b>

- 1 <= s.length <= 10^5
- s[i] is one of  '(' , ')' and lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_index = set()
        st = []
        for i,ch in enumerate(s):
            if ch not in '()':
                continue
            if ch == '(':
                st.append(i)
            elif not st:
                remove_index.add(i)
            else:
                st.pop()
        
        remove_index = remove_index.union(set(st))
        new_s = []
        for i,ch in enumerate(s):
            if i not in remove_index:
                new_s.append(ch)
        return "".join(new_s)
```
