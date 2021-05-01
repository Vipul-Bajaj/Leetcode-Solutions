<h1>Min Stack</h1>

<p>
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

</p>

<b>Example 1:</b>

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
 
<b>Constraints:</b>

- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.stack.append(self.minimum)
            self.minimum = val
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            pass
        else:
            t = self.stack[-1]
            self.stack.pop()
            if self.minimum == t:
                self.minimum = self.stack[-1]
                self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
            
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
