# [Home](./../..)/[Amazon](./..)/[Medium](./)/Valid_Sudoku
<h1>Valid Sudoku</h1>

<p>
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
</p>

* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 
Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
</p>

<b>Example 1:</b>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png">

    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
    
<b>Example 2:</b>

    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


<b>Constraints:</b>

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.

<h2>Solution</h2>

```python
class Solution:
    def is_used_in_row(self,board,row,col):
        for i in range(9):
            if i!= col and board[row][i] != '.' and int(board[row][i]) == int(board[row][col]) :
                return True
        return False
    
    def is_used_in_col(self,board,row,col):
        for i in range(9):
            if i!= row and board[i][col] != '.' and int(board[i][col]) == int(board[row][col]):
                return True
        return False
        
    def is_used_in_box(self,board,row,col):
        box_x = row // 3
        box_y = col // 3
    
        for i in range(box_x*3, box_x*3 + 3):
            for j in range(box_y * 3, box_y*3 + 3):
                if i!=row and j!=col and board[i][j] != '.' and int(board[i][j]) == int(board[row][col]):
                    return True
        return False    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if self.is_used_in_row(board,i,j) or self.is_used_in_col(board,i,j) or self.is_used_in_box(board,i,j):
                        return False
        return True
```
