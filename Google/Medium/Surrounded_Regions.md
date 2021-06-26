# [Home](./../..)/[Google](./..)/[Medium](./)/Surrounded_Regions
<h1>Surrounded Regions</h1>

<p>
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
</p>
<p>
A region is captured by flipping all 'O's into 'X's in that surrounded region.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg">

    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
 
<b>Example 2:</b>

    Input: board = [["X"]]
    Output: [["X"]]

<b>Constraints:</b>

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.=

<h2>Solution</h2>

```python
class Solution:
    def flood_fill(self,board,rows,cols,i,j,previous_value,new_value):
        if i<0 or i>=rows or j<0 or j>=cols or board[i][j]!=previous_value:
            return 
        board[i][j] = new_value
        self.flood_fill(board,rows,cols,i+1,j,previous_value,new_value)
        self.flood_fill(board,rows,cols,i-1,j,previous_value,new_value)
        self.flood_fill(board,rows,cols,i,j+1,previous_value,new_value)
        self.flood_fill(board,rows,cols,i,j-1,previous_value,new_value)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j] = '-'
                    
        for i in range(m):
            if board[i][0] == '-':
                self.flood_fill(board,m,n,i,0,'-','O')
        
        for i in range(m):
            if board[i][n-1] == '-':
                self.flood_fill(board,m,n,i,n-1,'-','O')
                
        for j in range(n):
            if board[0][j] == '-':
                self.flood_fill(board,m,n,0,j,'-','O')
        
        for j in range(n):
            if board[m-1][j] == '-':
                self.flood_fill(board,m,n,m-1,j,'-','O')
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='-':
                    board[i][j] = 'X'
        
        return board
```
