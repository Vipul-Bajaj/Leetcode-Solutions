# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Two_City_Scheduling
<h1>Two City Scheduling</h1>

<p>
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
</p>
<p>
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
</p>

<b>Example 1:</b>

    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

<b>Example 2:</b>

    Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    Output: 1859
    
<b>Example 3:</b>

    Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    Output: 3086

<b>Constraints:</b>

- 2 * n == costs.length
- 2 <= costs.length <= 100
- costs.length is even.
- 1 <= aCosti, bCosti <= 1000

<h2>Solution</h2>

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[1]-x[0]))
        cost = 0
        for i in range(len(costs)):
            if i<len(costs)//2:
                cost+=costs[i][1]
            else:
                cost+=costs[i][0]
        return cost
```
