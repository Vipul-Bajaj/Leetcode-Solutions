<h1>Coin Change 2</h1>

<p>
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

</p>

<b>Example 1:</b>

    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    
<b>Example 2:</b>

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
    
<b>Example 3:</b>

    Input: amount = 10, coins = [10]
    Output: 1
    
<b>Constraints:</b>

- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000]

<h2>Solution</h2>

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(coins[i],amount+1):
                dp[j] += dp[j-coins[i]]
            print(dp)
        return dp[amount]
```
