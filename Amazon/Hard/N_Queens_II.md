# [Home](./../..)/[Amazon](./..)/[Hard](./)/N_Queens_II
<h1>N-Queens II</h1>

<p>
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg">

    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
    
<b>Example 2:</b>

    Input: n = 1
    Output: 1

<b>Constraints:</b>

- 1<=n<=9

<h2>Solution</h2>

```python
class Solution:
    def isSafe(self,board,row,col,n):
        for i in range(n):
            if i == row:
                continue
            if board[i][col] == 'Q':
                return False
        for j in range(n):
            if j == col:
                continue
            if board[row][j] == 'Q':
                return False
        i = row+1
        j = col+1
        while i<n and j<n:
            if board[i][j] == 'Q':
                return False
            i+=1
            j+=1
        i = row-1
        j = col-1
        while i>-1 and j>-1:
            if board[i][j] == 'Q':
                return False
            i-=1
            j-=1
        i = row+1
        j = col-1
        while i<n and j>-1:
            if board[i][j] == 'Q':
                return False
            i+=1
            j-=1
        i = row-1
        j = col+1
        while i>-1 and j<n:
            if board[i][j] == 'Q':
                return False
            i-=1
            j+=1
        return True
    def solve(self,board,col,n,res):
        if col>=n:
            res[0]+=1
            return True
        r = False
        for i in range(n):
            if self.isSafe(board,i,col,n):
                board[i][col] = 'Q'
                r = self.solve(board,col+1,n,res) or r
                board[i][col] = '.'
        return r
    def totalNQueens(self, n: int) -> int:
        board = [['.' for j in range(n)]for i in range(n)]
        res = [0]
        self.solve(board,0,n,res)
        return res[0]
```
