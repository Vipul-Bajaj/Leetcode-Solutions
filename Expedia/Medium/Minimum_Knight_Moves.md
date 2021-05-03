# [Home](./../../..)/[Expedia](./../..)/[Medium](./..)/Minimum_Knight_Moves
<h1>Minimum Knight Moves</h1>

<p>
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

<img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png">

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

</p>

<b>Example 1:</b>

    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]
    
<b>Example 2:</b>

    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

<b>Constraints:</b>

- |x| + |y| <= 300

<h2>Solution</h2>

```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirt = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
        pos = (0,0)
        target = (x,y)

        q = deque([(pos,0)])
        visited = set()
        min_moves = 2**31
        visited.add(pos)
        while q:
            pos,moves = q.popleft()
            if pos == target:
                min_moves = min(min_moves,moves)
                break
            visited.add(pos)
            moves+=1
            x,y = pos
            for n_x,n_y in dirt:
                if (x+n_x,y+n_y) not in visited:
                    visited.add((x+n_x,y+n_y))
                    q.append(((x+n_x,y+n_y),moves))
        return min_moves
```
