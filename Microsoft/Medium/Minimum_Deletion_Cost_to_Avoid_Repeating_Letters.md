# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Minimum_Deletion_Cost_to_Avoid_Repeating_Letters
<h1>Minimum Deletion Cost to Avoid Repeating Letters</h1>

<p>
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.
</p>

<b>Example 1:</b>

    Input: s = "abaac", cost = [1,2,3,4,5]
    Output: 3
    Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
    
<b>Example 2:</b>

    Input: s = "abc", cost = [1,2,3]
    Output: 0
    Explanation: You don't need to delete any character because there are no identical letters next to each other.
    
<b>Example 3:</b>
    
    Input: s = "aabaa", cost = [1,2,3,4,1]
    Output: 2
    Explanation: Delete the first and the last character, getting the string ("aba").

<b>Constraints:</b>

- s.length == cost.length
- 1 <= s.length, cost.length <= 10^5
- 1 <= cost[i] <= 10^4
- s contains only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # n = len(s)
        # i = 0
        # min_cost = 0
        # while i<n:
        #     temp = i+1
        #     while temp<n and s[i] == s[temp]:
        #         min_cost += min(cost[i],cost[temp])
        #         i = temp if cost[i]<=cost[temp] else i
        #         temp+=1
        #     i = temp
        # return min_cost
        prev = s[0]
        prevCost = cost[0]
        curCost = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                if cost[i] < prevCost:
                    curCost += cost[i]
                else:
                    curCost += prevCost
                    prevCost = cost[i]
            else:
                prevCost = cost[i]      
            prev = s[i]
        return curCost
```
