# [Home](./../..)/[Qualcomm](./..)/[Easy](./)/Remove_Outermost_Parentheses
<h1>Remove Outermost Parentheses</h1>

<p>
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
</p>
<p>
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A+B, with A and B nonempty valid parentheses strings.
</p>
<p>
Given a valid parentheses string s, consider its primitive decomposition: s = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
</p>
<p>
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
</p>

<b>Example 1:</b>

    Input: s = "(()())(())"
    Output: "()()()"
    Explanation: 
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
    
<b>Example 2:</b>

    Input: s = "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation: 
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

<b>Example 3:</b>

    Input: s = "()()"
    Output: ""
    Explanation: 
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".

<b>Constraints:</b>

- s.length <= 10000
- s[i] is "(" or ")"
- s is a valid parentheses string

<h2>Solution</h2>

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        out = []
        c= 0
        for ch in s:
            if ch == '(':
                st.append('(')
                c+=1
                if c!=1:
                    out.append('(')
            else:
                if c == 1:
                    st.pop()
                    c-=1
                    continue
                st.pop()
                out.append(')')
                c-=1
        return "".join(out)
```
