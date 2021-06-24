# [Home](./../..)/[Directi](./..)/[Medium](./)/Find_the_Winner_of_an_Array_Game
<h1>Find the Winner of an Array Game</h1>

<p>
Given an integer array arr of distinct integers and an integer k.
</p>
<p>
A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
</p>
<p>
Return the integer which will win the game.
</p>
<p>
It is guaranteed that there will be a winner of the game.
</p>

<b>Example 1:</b>

    Input: arr = [2,1,3,5,4,6,7], k = 2
    Output: 5
    Explanation: Let's see the rounds of the game:
    Round |       arr       | winner | win_count
      1   | [2,1,3,5,4,6,7] | 2      | 1
      2   | [2,3,5,4,6,7,1] | 3      | 1
      3   | [3,5,4,6,7,1,2] | 5      | 1
      4   | [5,4,6,7,1,2,3] | 5      | 2
    So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
    
<b>Example 2:</b>

    Input: arr = [3,2,1], k = 10
    Output: 3
    Explanation: 3 will win the first 10 rounds consecutively.
    
<b>Example 3:</b>

    Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
    Output: 99

<b>Constraints:</b>

- 2 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^6
- arr contains distinct integers.
- 1 <= k <= 10^9

<h2>Solution</h2>

```python
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        winner = arr[0]
        for i in range(1,len(arr)):
            if winner>arr[i]:
                wins+=1
            else:
                wins = 1
                winner = arr[i]
            if wins==k:
                break
        return winner
```
