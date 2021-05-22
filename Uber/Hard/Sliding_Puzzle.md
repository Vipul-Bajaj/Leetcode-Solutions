# [Home](./../..)/[Uber](./..)/[Hard](./)/Sliding_Puzzle
<h1>Sliding Puzzle</h1>

<p>
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
</p>
<p>
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
</p>
<p>
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
</p>
<p>
Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
</p>

<b>Example 1:</b>

    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.
    
<b>Example 2:</b>

    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.
    
<b>Example 3:</b>

    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]
    
<b>Example 4:</b>

    Input: board = [[3,2,4],[1,5,0]]
    Output: 14

<b>Constraints:</b>

- board will be a 2 x 3 array as described above.
- board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

<h2>Solution</h2>

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves_allowed = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        
        state = list(c for c in board[0]+board[1])
        visited = set()
        start = state.index(0)
        
        q = deque([(start, state, 0)])
        
        while q:
            curr,state, steps = q.popleft()
            if state == [1,2,3,4,5,0]:
                return steps
            elif tuple(state) in visited:
                continue
            else:
                visited.add(tuple(state))
                for pos in moves_allowed[curr]:
                    temp = state.copy()
                    temp[pos],temp[curr] = temp[curr],temp[pos]
                    q.append((pos,temp,steps+1))
                    
        return -1
```
