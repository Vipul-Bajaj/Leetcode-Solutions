# [Home](./../../..)/[Expedia](./../..)/[Easy](./..)/Climbing_Stairs
<h1>Climbing Stairs</h1>

<p>
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

</p>

<b>Example 1:</b>

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
<b>Example 2:</b>

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

<b>Constraints:</b>

- 1 <= n <= 45

<h2>Solution</h2>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        s = 2
        i = 3
        if n == 1:
            return f
        if n == 2:
            return s
        while i<=n:
            t = f+s
            f = s
            s = t
            i+=1
        return s
```
