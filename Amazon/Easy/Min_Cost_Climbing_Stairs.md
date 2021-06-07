# [Home](./../..)/[Amazon](./..)/[Easy](./)/Min_Cost_Climbing_Stairs
<h1>Min Cost Climbing Stairs</h1>

<p>
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
</p>
<p>
You can either start from the step with index 0, or the step with index 1.
</p>
<p>
Return the minimum cost to reach the top of the floor.
</p>

<b>Example 1:</b>

    Input: cost = [10,15,20]
    Output: 15
    Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
    
<b>Example 2:</b>

    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
    
<b>Constraints:</b>

- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999

<h2>Solution</h2>

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        i = n-3
        while i>=0:
            cost[i] = cost[i] + min(cost[i+1],cost[i+2])
            i-=1
        return min(cost[0],cost[1])
```
