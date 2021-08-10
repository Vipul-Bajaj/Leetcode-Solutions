# [Home](./../..)/[Amazon](./..)/[Medium](./)/Reach_a_Number
<h1>Reach a Number</h1>

<p>
You are standing at position 0 on an infinite number line. There is a destination at position target.
</p>
<p>
You can make some number of moves numMoves so that:
</p>

- On each move, you can either go left or right.
- During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.

<p>
Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.
</p>

<b>Example 1:</b>

    Input: target = 2
    Output: 3
    Explanation:
    On the 1st move, we step from 0 to 1 (1 step).
    On the 2nd move, we step from 1 to -1 (2 steps).
    On the 3rd move, we step from -1 to 2 (3 steps).

<b>Example 2:</b>

    Input: target = 3
    Output: 2
    Explanation:
    On the 1st move, we step from 0 to 1 (1 step).
    On the 2nd move, we step from 1 to 3 (2 steps).
<b>Constraints:</b>

- -109 <= target <= 109
- target != 0

<h2>Solution</h2>

```python
class Solution:
    def reachNumber(self, target: int) -> int:
        ans, k = 0, 0
        target = abs(target)
        while ans < target:
            ans += k
            k += 1
        while (ans - target) % 2:
            ans += k
            k += 1
        return k - 1  
```
