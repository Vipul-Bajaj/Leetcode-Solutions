# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Coin_Change
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Coin_Change
<h1>Coin Change</h1>

<p>
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

</p>

<b>Example 1:</b>

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    
<b>Example 2:</b>

    Input: coins = [2], amount = 3
    Output: -1
    
<b>Example 3:</b>

    Input: coins = [1], amount = 0
    Output: 0

<b>Constraints:</b>

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 231 - 1
- 0 <= amount <= 104

<h2>Solution</h2>

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        dp = [2**31]* (amount+1)
        
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != 2**31 else -1
```
