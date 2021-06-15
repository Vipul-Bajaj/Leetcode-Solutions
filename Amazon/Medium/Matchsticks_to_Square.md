# [Home](./../..)/[Amazon](./..)/[Medium](./)/Matchsticks_to_Square
<h1>Matchsticks to Square</h1>

<p>
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
</p>
<p>
Return true if you can make this square and false otherwise.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg">

    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
    
<b>Example 2:</b>

    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.

<b>Constraints:</b>

- 1 <= matchsticks.length <= 15
- 0 <= matchsticks[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        peri = sum(matchsticks)
        n = len(matchsticks)
        side = peri//4
        if side*4 != peri:
            return False
        matchsticks.sort(reverse=True)
        
        sides = [0]*4
        
        def dfs(index):
            if index==n:
                return sides[0]==sides[1]==sides[2]==side
            for i in range(4):
                if sides[i]+matchsticks[index]<=side:
                    sides[i]+=matchsticks[index]
                    if dfs(index+1):
                        return True
                    sides[i]-=matchsticks[index]
            return False
        return dfs(0)
```
