# [Home](./../..)/[Microsoft](./..)/[Hard](./)/Sudoku_Solver
<h1>Sudoku Solver</h1>

<p>
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
</p>

- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
</p>

<b>Example 1:</b>
  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png">  

    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Explanation: The input board is shown above and the only valid solution is shown below:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png">
<b>Constraints:</b>

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.

<h2>Solution</h2>

```python
class Solution:
    def has_empty_space(self,board,empty):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty[0],empty[1] = i,j
                    return True           
        return False
    
    def is_used_in_row(self,board,row,num):
        for i in range(9):
            if board[row][i] != '.' and int(board[row][i]) == num:
                return True
        return False
    
    def is_used_in_col(self,board,col,num):
        for i in range(9):
            if board[i][col] != '.' and int(board[i][col]) == num:
                return True
        return False
        
    def is_used_in_box(self,board,row,col,num):
        box_x = row // 3
        box_y = col // 3
    
        for i in range(box_x*3, box_x*3 + 3):
            for j in range(box_y * 3, box_y*3 + 3):
                if board[i][j] != '.' and int(board[i][j]) == num:
                    return True
        return False    
    
    def check_if_is_safe(self,board,row,col,num):
        return not self.is_used_in_row(board,row, num) and not self.is_used_in_col(board,col, num) and not self.is_used_in_box(board,row,col, num)
    
    def solve(self,board):
        empty = [0,0]
        
        if not self.has_empty_space(board,empty):
            return True
        
        row,col = empty
        
        for num in range(1,10):
            if self.check_if_is_safe(board,row,col,num):
                board[row][col] = str(num)
                if self.solve(board):
                    return True
                board[row][col] = "."
        return False
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
```
