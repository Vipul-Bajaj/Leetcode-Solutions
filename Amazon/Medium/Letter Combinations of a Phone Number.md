<h1>Letter Combinations of a Phone Number</h1>

<p>
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png">

<b>Example 1:</b>

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
<b>Example 2:</b>

    Input: digits = ""
    Output: []
    
<b>Example 3:</b>

    Input: digits = "2"
    Output: ["a","b","c"]

<b>Constraints:</b>

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

<h2>Solution</h2>

```python
class Solution:
    def solve(self,digits,s):
        if len(digits) == 0:
            self.res.append("".join(s))
            return self.res
        for i in self.mapping[digits[0]]:
            s.append(i)
            self.solve(digits[1:],s)
            s.pop(-1)
        return self.res
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        if len(digits)==0:
            return []
        self.mapping = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        
        return self.solve(digits,[])
```
