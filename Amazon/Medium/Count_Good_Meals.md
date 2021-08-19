# [Home](./../..)/[Amazon](./..)/[Medium](./)/Count_Good_Meals
<h1>Count Good Meals</h1>

<p>
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
</p>
<p>
You can pick any two different foods to make a good meal.
</p>
<p>
Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.
</p>
<p>
Note that items with different indices are considered different even if they have the same deliciousness value.
</p>

<b>Example 1:</b>

    Input: deliciousness = [1,3,5,7,9]
    Output: 4
    Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
    Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

<b>Example 2:</b>

    Input: deliciousness = [1,1,1,3,3,3,7]
    Output: 15
    Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.

<b>Constraints:</b>

- 1 <= deliciousness.length <= 105
- 0 <= deliciousness[i] <= 220

<h2>Solution</h2>

```python
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)
        ans = 0
        for x in count: 
            for k in range(22): 
                if 2**k - x <= x and 2**k - x in count: 
                    ans += count[x]*(count[x]-1)//2 if 2**k - x == x else count[x]*count[2**k-x]
        return ans % 1_000_000_007
```
