# [Home](./../..)/[Google](./..)/[Medium](./)/Closest_Dessert_Cost
<h1>Closest Dessert Cost</h1>

<p>
You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:
</p>

- There must be exactly one ice cream base.
- You can add one or more types of topping or have no toppings at all.
- There are at most two of each type of topping.

<p>
You are given three inputs:
</p>

- baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
- toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
- target, an integer representing your target price for dessert.

<p>
You want to make a dessert with a total cost as close to target as possible.
</p>
<p>
Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.
</p>

<b>Example 1:</b>

    Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
    Output: 10
    Explanation: Consider the following combination (all 0-indexed):
    - Choose base 1: cost 7
    - Take 1 of topping 0: cost 1 x 3 = 3
    - Take 0 of topping 1: cost 0 x 4 = 0
    Total: 7 + 3 + 0 = 10.

<b>Example 2:</b>

    Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
    Output: 17
    Explanation: Consider the following combination (all 0-indexed):
    - Choose base 1: cost 3
    - Take 1 of topping 0: cost 1 x 4 = 4
    - Take 2 of topping 1: cost 2 x 5 = 10
    - Take 0 of topping 2: cost 0 x 100 = 0
    Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

<b>Example 3:</b>

    Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
    Output: 8
    Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

<b>Example 4:</b>

    Input: baseCosts = [10], toppingCosts = [1], target = 1
    Output: 10
    Explanation: Notice that you don't have to have any toppings, but you must have exactly one base.

<b>Constraints:</b>

- n == baseCosts.length
- m == toppingCosts.length
- 1 <= n, m <= 10
- 1 <= baseCosts[i], toppingCosts[i] <= 104
- 1 <= target <= 104

<h2>Solution</h2>

```python
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        dairy = {}
        
        def possibleprices(cost,ind):
            if abs(target-cost) in dairy: 
                if dairy[abs(target-cost)] > cost:
                    dairy[abs(target-cost)] = cost 
            else:
                dairy[abs(target-cost)] = cost
            if ind>=len(toppingCosts) or cost-target > min(dairy):
                return
            possibleprices(cost,ind+1)
            possibleprices(cost+toppingCosts[ind],ind+1)
            possibleprices(cost+(toppingCosts[ind]*2),ind+1)
            
        for base in baseCosts:
            curCost = base 
            possibleprices(curCost,0)
        return dairy[min(dairy)]
```
