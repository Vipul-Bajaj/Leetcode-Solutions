# [Home](./../..)/[Facebook](./..)/[Medium](./)/Battleships_in_a_Board
<h1>Battleships in a Board</h1>

<p>
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg">

    Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    Output: 2
    
<b>Example 2:</b>

    Input: board = [["."]]
    Output: 0

<b>Constraints:</b>

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is either '.' or 'X'.

<b>Follow up:</b>

Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

<h2>Solution</h2>

```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count
```
