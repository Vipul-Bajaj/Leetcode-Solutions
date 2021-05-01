<h1>Fizz Buzz</h1>

<p>
Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i if non of the above conditions are true.

</p>

<b>Example 1:</b>

    Input: n = 3
    Output: ["1","2","Fizz"]
    
<b>Example 2:</b>

    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]
    
<b>Example 3:</b>

    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

<b>Constraints:</b>

- 1 <= n <= 104

<h2>Solution</h2>

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1,n+1):
            if i%3 == 0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
```
