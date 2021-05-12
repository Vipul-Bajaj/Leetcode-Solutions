# [Home](./../..)/[Adobe](./..)/[Easy](./)/Divisor_Game
<h1>Divisor Game</h1>

<p>
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
</p>

- Choosing any x with 0 < x < n and n % x == 0.
- Replacing the number n on the chalkboard with n - x.
- Also, if a player cannot make a move, they lose the game.

<p>
Return true if and only if Alice wins the game, assuming both players play optimally.
</p>

<b>Example 1:</b>

    Input: n = 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.
    
<b>Example 2:</b>

    Input: n = 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

<b>Constraints:</b>

- 1 <= n <= 1000

<h2>Solution</h2>

```python
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2==0
```
