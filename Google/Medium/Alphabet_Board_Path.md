# [Home](./../..)/[Google](./..)/[Medium](./)/Alphabet_Board_Path
<h1>Alphabet Board Path</h1>

<p>
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
</p>
<p>
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.
</p>

<img src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png">

<p>
We may make the following moves:
</p>

- 'U' moves our position up one row, if the position exists on the board;
- 'D' moves our position down one row, if the position exists on the board;
- 'L' moves our position left one column, if the position exists on the board;
- 'R' moves our position right one column, if the position exists on the board;
- '!' adds the character board[r][c] at our current position (r, c) to the answer.

<p>
(Here, the only positions that exist on the board are positions with letters on them.)
</p>
<p>
Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.
</p>

<b>Example 1:</b>

    Input: target = "leet"
    Output: "DDR!UURRR!!DDD!"

<b>Example 2:</b>

    Input: target = "code"
    Output: "RR!DDRR!UUL!R!"
    
<b>Constraints:</b>

- 1 <= target.length <= 100
- target consists only of English lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)
```
