# [Home](./../..)/[Google](./..)/[Easy](./)/Flip_Game
<h1>Flip Game</h1>

<p>
You are playing a Flip Game with your friend.
</p>
<p>
You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.
</p>
<p>
Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].
</p>

<b>Example 1:</b>

    Input: currentState = "++++"
    Output: ["--++","+--+","++--"]

<b>Example 2:</b>

    Input: currentState = "+"
    Output: []
    
<b>Constraints:</b>

- 1 <= currentState.length <= 500
- currentState[i] is either '+' or '-'.

<h2>Solution</h2>

```python
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        out = []
        for i in range(len(currentState)-1):
            if currentState[i]+currentState[i+1] == "++":
                out.append(currentState[:i]+"--"+currentState[i+2:])
        return out
```
