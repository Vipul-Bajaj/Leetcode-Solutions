# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Generate_Parentheses
<h1>Generate Parentheses</h1>

<p>
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

</p>

<b>Example 1:</b>

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    
<b>Example 2:</b>

    Input: n = 1
    Output: ["()"]
    
<b>Constraints:</b>

- 1 <= n <= 8

<h2>Solution</h2>

```python
class Solution:
    def generate(self,open_b,close_b,s):
        if open_b == 0 and close_b == 0:
            self.res.append(s)
            return
        if open_b>close_b:
            return
        if open_b>0:
            self.generate(open_b-1,close_b,s+"(")
        if close_b>0:
            self.generate(open_b,close_b-1,s+")")
        return
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generate(n,n,"")
        return self.res
```
