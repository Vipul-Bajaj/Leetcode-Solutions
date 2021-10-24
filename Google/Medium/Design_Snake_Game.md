# [Home](./../..)/[Google](./..)/[Medium](./)/Design_Snake_Game
<h1>Design Snake Game</h1>

<p>
Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.
</p>
<p>
The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.
</p>
<p>
You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.
</p>
<p>
Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.
</p>
<p>
When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
</p>
<p>
The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).
</p>
<p>
Implement the SnakeGame class:
</p>

- SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
- int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.


<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/13/snake.jpg">

    Input
    ["SnakeGame", "move", "move", "move", "move", "move", "move"]
    [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
    Output
    [null, 0, 0, 1, 1, 2, -1]

    Explanation
    SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
    snakeGame.move("R"); // return 0
    snakeGame.move("D"); // return 0
    snakeGame.move("R"); // return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
    snakeGame.move("U"); // return 1
    snakeGame.move("L"); // return 2, snake eats the second food. No more food appears.
    snakeGame.move("U"); // return -1, game over because snake collides with border
    
<b>Constraints:</b>

- 1 <= width, height <= 104
- 1 <= food.length <= 50
- food[i].length == 2
- 0 <= ri < height
- 0 <= ci < width
- direction.length == 1
- direction is 'U', 'D', 'L', or 'R'.
- At most 104 calls will be made to move.

<h2>Solution</h2>

```python
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.food_arr = food
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0,0)])
        self.directions = {
            'R': (0,1),
            'L': (0,-1),
            'U': (-1,0),
            'D': (1,0)
        }
        self.food_idx = 0

    def move(self, direction: str) -> int:
        new_head = self.snake[0][0]+self.directions[direction][0], self.snake[0][1]+self.directions[direction][1]
        
        crosses_heights = new_head[0]<0 or new_head[0]>=self.height
        crosses_widths = new_head[1]<0 or new_head[1]>=self.width
        
        bites_itself = new_head in self.snake_set and new_head != self.snake[-1]
        
        if crosses_heights or crosses_widths or bites_itself:
            return -1
        
        next_food_item = self.food_arr[self.food_idx] if self.food_idx < len(self.food_arr) else None
        
        if self.food_idx<len(self.food_arr) and next_food_item[0] == new_head[0] and next_food_item[1] == new_head[1]:
            self.food_idx+=1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)
        
        self.snake.appendleft(new_head)
        
        self.snake_set.add(new_head)
        
        return len(self.snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
```
