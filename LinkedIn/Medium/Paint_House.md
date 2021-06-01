# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Paint_House
<h1>Paint House</h1>

<p>
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
</p>
<p>
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
</p>

* For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

<p>
Return the minimum cost to paint all houses.
</p>

<b>Example 1:</b>

    Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
    Output: 10
    Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
    Minimum cost: 2 + 5 + 3 = 10.
    
<b>Example 2:</b>

    Input: costs = [[7,6,2]]
    Output: 2

<b>Constraints:</b>

- costs.length == n
- costs[i].length == 3
- 1 <= n <= 100
- 1 <= costs[i][j] <= 20

<h2>Solution</h2>

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        r, g, b = 0, 0, 0
        
        for i in range(len(costs)):
            r, g, b = costs[i][0] + min(g, b), costs[i][1] + min(r, b), costs[i][2] + min(g, r)
        
        return min(r, g, b)
```
