<h1>Evaluate Reverse Polish Notation</h1>

<p>
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

</p>

<b>Example 1:</b>

    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    
<b>Example 2:</b>

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
    
<b>Example 3:</b>

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

<b>Constraints:</b>

- 1 <= tokens.length <= 104
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

<h2>Solution</h2>

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                operand.append(int(i))
            else:
                ele2 = operand.pop()
                ele1 = operand.pop()
                sign1 = 1 if ele1 >= 0 else -1
                sign2 = 1 if ele2 >= 0 else -1
                
                if i == '+':
                    ele1+=ele2
                elif i == '-':
                    ele1-=ele2
                elif i == '*':
                    ele1*=ele2
                elif i == '/':
                    ele1= abs(ele1)//abs(ele2)
                    ele1 = ele1*sign1*sign2
                operand.append(ele1)
        return operand[-1]
```
