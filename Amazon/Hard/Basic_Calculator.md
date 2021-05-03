# [Home](./../../..)/[Amazon](./../..)/[Hard](./..)/Basic_Calculator
<h1>Basic Calculator</h1>

<p>
Given a string s representing an expression, implement a basic calculator to evaluate it.

</p>

<b>Example 1:</b>

    Input: s = "1 + 1"
    Output: 2
    
<b>Example 2:</b>

    Input: s = " 2-1 + 2 "
    Output: 3
    
<b>Example 3:</b>

    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

<b>Constraints:</b>

- 1 <= s.length <= 3 * 105
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.

<h2>Solution</h2>

```python
class Solution:
    def evaluate(self,st):
        res = 0
        if st and type(st[-1]) == type(1):
            res = st.pop()
        
        while st and st[-1] != ')':
            opr = st.pop()
            if opr == '+':
                res += st.pop()
            else:
                res -= st.pop()
        return res
    def calculate(self, s: str) -> int:
        s = s[::-1]
        s = s.strip()
        st = []
        n,operand = 0,0
        
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                operand = (10**n * int(ch)) + operand
                n+=1
            elif ch != ' ':
                if n:
                    st.append(operand)
                    n,operand = 0,0
                if ch == '(':
                    res = self.evaluate(st)
                    st.pop()
                    st.append(res)
                else:
                    st.append(ch)
        if n:
            st.append(operand)
            
        return self.evaluate(st)
```
