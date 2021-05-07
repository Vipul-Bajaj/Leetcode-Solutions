# [Home](./../..)/[Goldman Sachs](./..)/[Medium](./)/Count_Number_of_Teams
<h1>Count Number of Teams</h1>

<p>
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

- Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
- A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
</p>

<b>Example 1:</b>

    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

<b>Example 2:</b>

    Input: rating = [2,1,3]
    Output: 0
    Explanation: We can't form any team given the conditions.
    
<b>Example 3:</b>

    Input: rating = [1,2,3,4]
    Output: 4
    
<b>Constraints:</b>

- n == rating.length
- 3 <= n <= 1000
- 1 <= rating[i] <= 105
- All the integers in rating are unique.

<h2>Solution</h2>

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        for i in range(1, len(rating) - 1):
            less1 = more1 = 0
            less2 = more2 = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    less1 += 1
                elif rating[j] > rating[i]:
                    less2 += 1
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    more1 += 1
                elif rating[j] < rating[i]:
                    more2 += 1            
            total += less1 * more1 + less2 * more2 

        return total
```
