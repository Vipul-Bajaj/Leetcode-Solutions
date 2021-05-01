<h1>Word Search</h1>

<p>
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg">

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg">

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg">

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

<b>Constraints:</b>

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def dfs(self,board,i,j,m,n,visited,word,idx,word_length):
        dirt = [[0,1],[1,0],[0,-1],[-1,0]]
        visited[i][j] = True
        if word_length == idx:
            return True
        found = False
        
        for d in dirt:
            new_i = i+d[0]
            new_j = j+d[1]
            if 0<=new_i<m and 0<=new_j<n and not visited[new_i][new_j] and board[new_i][new_j] == word[idx]:
                found = self.dfs(board,new_i,new_j,m,n,visited,word,idx+1,word_length) or found
                if found:
                    return found
        visited[i][j] = False
        
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(board),len(board[0])
        visited = [[False for j in range(n)] for i  in range(m)]
        found = False
        word_length = len(word)
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and word[0] == board[i][j]:
                    found = self.dfs(board,i,j,m,n,visited,word,1,word_length) or found
                    if found:
                        break
        return found
```
