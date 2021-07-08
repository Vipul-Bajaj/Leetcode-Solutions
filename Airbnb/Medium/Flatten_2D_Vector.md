# [Home](./../..)/[Airbnb](./..)/[Medium](./)/Flatten_2D_Vector
<h1>Flatten 2D Vector</h1>

<p>
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
<br>

Implement the Vector2D class:
</p>

* Vector2D(int[][] vec) initializes the object with the 2D vector vec.
* next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
* hasNext() returns true if there are still some elements in the vector, and false otherwise.

<b>Example 1:</b>

    Input
    ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
    [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
    Output
    [null, 1, 2, 3, true, true, 4, false]

    Explanation
    Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
    vector2D.next();    // return 1
    vector2D.next();    // return 2
    vector2D.next();    // return 3
    vector2D.hasNext(); // return True
    vector2D.hasNext(); // return True
    vector2D.next();    // return 4
    vector2D.hasNext(); // return False
<b>Constraints:</b>

- 0 <= vec.length <= 200
- 0 <= vec[i].length <= 500
- -500 <= vec[i][j] <= 500
- At most 105 calls will be made to next and hasNext.

<h2>Solution</h2>

```python
class Vector2D:

    def get_next_pointers(self):
        while self.row<len(self.vec) and self.col == len(self.vec[self.row]):
            self.row+=1
            self.col = 0
            
    def __init__(self, vec: List[List[int]]):
        self.row,self.col = 0,0
        self.vec = vec
        
    def next(self) -> int:
        self.get_next_pointers()
        ele = self.vec[self.row][self.col]
        self.col+=1
        return ele

    def hasNext(self) -> bool:
        self.get_next_pointers()
        return self.row<len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
