# [Home](./../..)/[Amazon](./..)/[Medium](./)/Number_of_Dice_Rolls_With_Target_Sum
<h1>Number of Dice Rolls With Target Sum</h1>

<p>
You have d dice and each die has f faces numbered 1, 2, ..., f.
</p>
<p>
Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.
</p>

<b>Example 1:</b>

    Input: d = 1, f = 6, target = 3
    Output: 1
    Explanation: 
    You throw one die with 6 faces.  There is only one way to get a sum of 3.

<b>Example 2:</b>

    Input: d = 2, f = 6, target = 7
    Output: 6
    Explanation: 
    You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
    1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

<b>Example 3:</b>

    Input: d = 2, f = 5, target = 10
    Output: 1
    Explanation: 
    You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

<b>Example 4:</b>

    Input: d = 1, f = 2, target = 3
    Output: 0
    Explanation: 
    You throw one die with 2 faces.  There is no way to get a sum of 3.

<b>Example 5:</b>

    Input: d = 30, f = 30, target = 500
    Output: 222616187
    Explanation: 
    The answer must be returned modulo 10^9 + 7.

<b>Constraints:</b>

- 1 <= d, f <= 30
- 1 <= target <= 1000

<h2>Solution</h2>

```python
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                    k += 1
        return dp[d][target] % mod
```
