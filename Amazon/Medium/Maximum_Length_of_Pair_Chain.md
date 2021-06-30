# [Home](./../..)/[Amazon](./..)/[Medium](./)/Maximum_Length_of_Pair_Chain
<h1>Maximum Length of Pair Chain</h1>

<p>
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
</p>
<p>
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
</p>
<p>
Return the length longest chain which can be formed.
</p>
<p>
You do not need to use up all the given intervals. You can select pairs in any order.
</p>

<b>Example 1:</b>

    Input: pairs = [[1,2],[2,3],[3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4].
    
<b>Example 2:</b>

    Input: pairs = [[1,2],[7,8],[4,5]]
    Output: 3
    Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

<b>Constraints:</b>

- n == pairs.length
- 1 <= n <= 1000
- -1000 <= lefti < righti < 1000

<h2>Solution</h2>

```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        ans,curr = 0,float('-inf')
        for x,y in pairs:
            if curr<x:
                ans+=1
                curr = y
        return ans
```
