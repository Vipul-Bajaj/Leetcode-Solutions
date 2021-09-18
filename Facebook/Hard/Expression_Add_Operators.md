# [Home](./../..)/[Facebook](./..)/[Hard](./)/Expression_Add_Operators
<h1>Expression Add Operators</h1>

<p>
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.
</p>

<b>Example 1:</b>

    Input: num = "123", target = 6
    Output: ["1*2*3","1+2+3"]

<b>Example 2:</b>

    Input: num = "232", target = 8
    Output: ["2*3+2","2+3*2"]

<b>Example 3:</b>

    Input: num = "105", target = 5
    Output: ["1*0+5","10-5"]

<b>Example 4:</b>

    Input: num = "00", target = 0
    Output: ["0*0","0+0","0-0"]

<b>Example 5:</b>

    Input: num = "3456237490", target = 9191
    Output: []

<b>Constraints:</b>

- 1 <= num.length <= 10
- num consists of only digits.
- -231 <= target <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        answer = []
        
        def backtrack(index, prev, curr, value, exp):
            if index == n:
                if value == target and curr == 0:
                    answer.append("".join(exp[1:]))
                return
            
            curr = curr*10 + int(num[index])
            str_op = str(curr)
            
            if curr>0:
                backtrack(index+1,prev,curr,value,exp)
            
            exp.append('+')
            exp.append(str_op)
            backtrack(index+1,curr,0,value+curr,exp)
            exp.pop();
            exp.pop();
            
            if exp:
                exp.append('-')
                exp.append(str_op)
                backtrack(index+1,-curr,0,value-curr,exp)
                exp.pop();
                exp.pop();
                
                exp.append('*')
                exp.append(str_op)
                backtrack(index+1,curr*prev,0,value-prev + (curr*prev),exp)
                exp.pop();
                exp.pop();
        backtrack(0,0,0,0,[])
        return answer
```
