# [Home](./../..)/[Amazon](./..)/[Medium](./)/Sell_Diminishing_Valued_Colored_Balls
<h1>Sell Diminishing-Valued Colored Balls</h1>

<p>
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.
</p>
<p>
The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).
</p>
<p>
You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.
</p>
<p>
Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/jj.gif">

    Input: inventory = [2,5], orders = 4
    Output: 14
    Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
    The maximum total value is 2 + 5 + 4 + 3 = 14.
    
<b>Example 2:</b>

    Input: inventory = [3,5], orders = 6
    Output: 19
    Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
    The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
    
<b>Example 3:</b>

    Input: inventory = [1000000000], orders = 1000000000
    Output: 21
    Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.

<b>Constraints:</b>

- 1 <= inventory.length <= 105
- 1 <= inventory[i] <= 109
- 1 <= orders <= min(sum(inventory[i]), 109)

<h2>Solution</h2>

```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) 
        inventory += [0]
        res = 0
        k = 1
        
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i]-inventory[i+1]) < orders:
                    diff = inventory[i]-inventory[i+1]
                    res += k*(inventory[i]+inventory[i+1]+1)*(diff)//2
                    orders -= k*diff
                else: 
                    q, r = divmod(orders, k)
                    res += k*(inventory[i]+(inventory[i]-q+1))*q//2
                    res += r*(inventory[i]-q)
                    return res%(10**9+7)
            k += 1
```
