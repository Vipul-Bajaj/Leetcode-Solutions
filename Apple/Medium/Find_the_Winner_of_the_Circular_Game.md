# [Home](./../..)/[Apple](./..)/[Medium](./)/Find_the_Winner_of_the_Circular_Game
<h1>Find the Winner of the Circular Game</h1>

<p>
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.
</p>
<p>
The rules of the game are as follows:
</p>

- Start at the 1st friend.
- Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
- The last friend you counted leaves the circle and loses the game.
- If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
- Else, the last friend in the circle wins the game.

<p>
Given the number of friends, n, and an integer k, return the winner of the game.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png">

    Input: n = 5, k = 2
    Output: 3
    Explanation: Here are the steps of the game:
    1) Start at friend 1.
    2) Count 2 friends clockwise, which are friends 1 and 2.
    3) Friend 2 leaves the circle. Next start is friend 3.
    4) Count 2 friends clockwise, which are friends 3 and 4.
    5) Friend 4 leaves the circle. Next start is friend 5.
    6) Count 2 friends clockwise, which are friends 5 and 1.
    7) Friend 1 leaves the circle. Next start is friend 3.
    8) Count 2 friends clockwise, which are friends 3 and 5.
    9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

<b>Example 2:</b>

    Input: n = 6, k = 5
    Output: 1
    Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

<b>Constraints:</b>

- 1 <= pattern.length <= 20
- 1 <= words.length <= 50
- words[i].length == pattern.length
- pattern and words[i] are lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # arr = list(range(1,n+1))
        # j=0
        # while len(arr)>1:
        #     j=(j+k-1)%len(arr)
        #     del arr[j]
        # return arr[0]
        res = 0
        
        for i in range(1, n + 1):
            res = (res + k) % i
            
        return res + 1
```
