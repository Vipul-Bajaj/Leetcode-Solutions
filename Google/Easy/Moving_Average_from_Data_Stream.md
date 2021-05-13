# [Home](./../..)/[Google](./..)/[Easy](./)/Moving_Average_from_Data_Stream
<h1>Moving Average from Data Stream</h1>

<p>
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
</p>

- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

<b>Example 1:</b>

    Input
    ["MovingAverage", "next", "next", "next", "next"]
    [[3], [1], [10], [3], [5]]
    Output
    [null, 1.0, 5.5, 4.66667, 6.0]

    Explanation
    MovingAverage movingAverage = new MovingAverage(3);
    movingAverage.next(1); // return 1.0 = 1 / 1
    movingAverage.next(10); // return 5.5 = (1 + 10) / 2
    movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
    movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

<b>Constraints:</b>
- 1 <= size <= 1000
- -105 <= val <= 105
- At most 104 calls will be made to next.

<h2>Solution</h2>

```python
"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque([])
        self.size = size
        self.c = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        tail = 0
        if self.c < self.size:
            self.c+=1
        else:
            tail = self.q.popleft()
        self.q.append(val)
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/min(self.size,self.c)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```
