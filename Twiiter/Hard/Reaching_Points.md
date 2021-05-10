# [Home](./../..)/[Twiiter](./..)/[Hard](./)/Reaching_Points
<h1>Reaching Points</h1>

<p>
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
</p>
<p>
Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
</p>

<b>Example 1:</b>

    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)

<b>Example 2:</b>

    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False
    
<b>Example 3:</b>

    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True


<b>Constraints:</b>

- sx, sy, tx, ty will all be integers in the range [1, 10^9].

<h2>Solution</h2>

```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and (ty - sy) % tx == 0:
                return True
            if ty == sy and (tx - sx) % ty == 0:
                return True
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        return False
```
