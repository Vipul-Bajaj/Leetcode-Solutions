# [Home](./../..)/[OT](./..)/[Hard](./)/Reducing_Dishes
<h1>Reducing Dishes</h1>

<p>
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
</p>

<b>Example 1:</b>

    Input: satisfaction = [-1,-8,0,5,-9]
    Output: 14
    Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.

<b>Example 2:</b>

    Input: satisfaction = [4,3,2]
    Output: 20
    Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
    
<b>Example 3:</b>

    Input: satisfaction = [-1,-4,-5]
    Output: 0
    Explanation: People don't like the dishes. No dish is prepared.
    
<b>Constraints:</b>

- n == satisfaction.length
- 1 <= n <= 500
- -10^3 <= satisfaction[i] <= 10^3

<h2>Solution</h2>

```python
# O(n^2) Solution
# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         n = len(satisfaction)
#         dp = [[0 for j in range(n)]for i in range(n)]
        
#         for i in range(n):
#             for j in range(i+1):
#                 dp[i][j] = satisfaction[i]*(j+1)
        
#         max_sum = 0
#         for k in range(n):
#             i = k
#             j = 0
#             s = 0
#             while i<n:
#                 s += dp[i][j]
#                 i+=1
#                 j+=1
#             # print(s)
#             max_sum = max(max_sum,s)
#         return max_sum

# O(nlogn) Solution
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:     
        satisfaction.sort()
        satis_sum = 0
        ans = 0
        i = len(satisfaction)-1
        while i >= 0 and satis_sum + satisfaction[i] > 0: 
            satis_sum += satisfaction[i]
            ans += satis_sum
            i -= 1
            
        return ans
```
