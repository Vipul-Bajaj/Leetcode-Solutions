# [Home](./../..)/[Dunzo](./..)/[Medium](./)/Stone_Game_VII
<h1>Stone Game VII</h1>

<p>
Alice and Bob take turns playing a game, with Alice starting first.
</p>
<p>
There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
</p>
<p>
Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.
</p>
<p>
Given an array of integers stones where stones[i] represents the value of the
</p>

<b>Example 1:</b>

    Input: stones = [5,3,1,4,2]
    Output: 6
    Explanation: 
    - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
    - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
    - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
    - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
    - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
    The score difference is 18 - 12 = 6.
    
<b>Example 2:</b>    

    Input: stones = [7,90,5,1,100,10,10,2]
    Output: 122

<b>Constraints:</b>

- n == stones.length
- 2 <= n <= 1000
- 1 <= stones[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0]*(n+1)
        
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1]+stones[i-1]
        
        dp = [[0 for j in range(n)] for i in range(n)]
        
        for start in range(n-2,-1,-1):
            for end in range(start+1,n):
                remove_from_first = prefix_sum[end+1]-prefix_sum[start+1]
                remove_from_last = prefix_sum[end]-prefix_sum[start]
                
                dp[start][end] = max(remove_from_first-dp[start+1][end],remove_from_last-dp[start][end-1])
                
        return dp[0][n-1]
```
