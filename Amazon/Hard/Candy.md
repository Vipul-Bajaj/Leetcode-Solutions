# [Home](./../..)/[Amazon](./..)/[Hard](./)/Candy
<h1>Candy</h1>

<p>
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
<br>
You are giving candies to these children subjected to the following requirements:
</p>

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

<p>
Return the minimum number of candies you need to have to distribute the candies to the children.
</p>

<b>Example 1:</b>

    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    
<b>Example 2:</b>

    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.

<b>Constraints:</b>

- n == ratings.length
- 1 <= n <= 2 * 104
- 0 <= ratings[i] <= 2 * 104

<h2>Solution</h2>

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(1,n):
            if ratings[i] == ratings[i-1]:
                continue
            elif ratings[i]>ratings[i-1] and candies[i]<=candies[i-1]:
                candies[i] = candies[i-1]+1
        s = candies[-1]
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1]+1)
            s+=candies[i]
        return s
```
