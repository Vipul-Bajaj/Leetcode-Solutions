# [Home](./../..)/[Amazon](./..)/[Medium](./)/Stone_Game
<h1>Stone_Game</h1>

<p>
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
</p>
<p>
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
</p>
<p>
Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
</p>
<p>
Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
</p>

<b>Example 1:</b>

    Input: piles = [5,3,4,5]
    Output: true
    Explanation: 
    Alex starts first, and can only take the first 5 or the last 5.
    Say he takes the first 5, so that the row becomes [3, 4, 5].
    If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
    If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
    This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
    
<b>Constraints:</b>

- 2 <= piles.length <= 500
- piles.length is even.
- 1 <= piles[i] <= 500
- sum(piles) is odd.

<h2>Solution</h2>

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for j in range(n+2)]for i in range(n+2)]
        
        for size in range(1,n+1):
            i = 0
            while i+size<=n:
                j = i+size-1
                parity = (i+j+n)%2
                if parity == 1:
                    dp[i+1][j+1] = max(piles[i]+dp[i+2][j+1],piles[j]+dp[i+1][j])
                else:
                    dp[i+1][j+1] = max(-piles[i]+dp[i+2][j+1],-piles[j]+dp[i+1][j])
                i+=1
                    
        return dp[1][n]>0
```
