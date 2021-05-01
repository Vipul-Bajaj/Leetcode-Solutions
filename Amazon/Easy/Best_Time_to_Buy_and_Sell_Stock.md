<h1>Best Time to Buy and Sell Stock</h1>

<p>
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

<b>Example 1:</b>

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
<b>Example 2:</b>

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

<b>Constraints:</b>

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

<h2>Solution</h2>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1:
            return 0
        max_profit = 0
        min_stock_value = prices[0]
        
        for i in range(1,n):
            if prices[i]<min_stock_value:
                min_stock_value = prices[i]
            if prices[i]-min_stock_value>max_profit:
                max_profit = prices[i]-min_stock_value
                
        return max_profit
```
