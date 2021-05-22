# [Home](./../..)/[Facebook](./..)/[Medium](./)/Minimum_Cost_For_Tickets
<h1>Minimum Cost For Tickets</h1>

<p>
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
<br>
Train tickets are sold in three different ways:
</p>

* a 1-day pass is sold for costs[0] dollars,
* a 7-day pass is sold for costs[1] dollars, and
* a 30-day pass is sold for costs[2] dollars.

<p>
The passes allow that many days of consecutive travel.
</p>

* For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

<p>
Return the minimum number of dollars you need to travel every day in the given list of days.
</p>

<b>Example 1:</b>

    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
    On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
    On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
    In total, you spent $11 and covered all the days of your travel.
    
<b>Example 2:</b>

    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
    On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
    In total, you spent $17 and covered all the days of your travel.

<b>Constraints:</b>

- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is in strictly increasing order.
- costs.length == 3
- 1 <= costs[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp  = [-1]*366
        
        for d in days:
            dp[d] = 0
        dp[0] = 0    
        for d in range(1,366):
            if dp[d] == -1:
                dp[d] = dp[d-1]
                continue
            dp[d] = min(dp[d-1]+costs[0],dp[max(d-7,0)]+costs[1],dp[max(d-30,0)]+costs[2])
        
        return dp[365]
```
