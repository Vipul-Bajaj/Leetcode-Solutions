# [Home](./../..)/[Google](./..)/[Medium](./)/Best_Time_to_Buy_and_Sell_Stock_II
<h1>Best Time to Buy and Sell Stock II</h1>

<p>
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
</p>
<p>
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
</p>
<p>
Find and return the maximum profit you can achieve.
</p>

<b>Example 1:</b>

    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.

<b>Example 2:</b>

    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Total profit is 4.

<b>Example 3:</b>

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
    
<b>Constraints:</b>

- 1 <= prices.length <= 3 * 104
- 0 <= prices[i] <= 104

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
            if prices[i]>min_stock_value:
                max_profit+=prices[i]-min_stock_value
                min_stock_value = 2**31
            if prices[i]<min_stock_value:
                min_stock_value = prices[i]
        
        return max_profit
```
