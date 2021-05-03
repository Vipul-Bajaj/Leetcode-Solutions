# [Home](./../..)/[Amazon](./..)/[Medium](./)/Design_Circular_Queue
<h1>Design Circular Queue</h1>

<p>
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

</p>

<b>Example 1:</b>

    Input
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 3, true, true, true, 4]

    Explanation
    MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    myCircularQueue.enQueue(1); // return True
    myCircularQueue.enQueue(2); // return True
    myCircularQueue.enQueue(3); // return True
    myCircularQueue.enQueue(4); // return False
    myCircularQueue.Rear();     // return 3
    myCircularQueue.isFull();   // return True
    myCircularQueue.deQueue();  // return True
    myCircularQueue.enQueue(4); // return True
    myCircularQueue.Rear();     // return 4

 
<b>Constraints:</b>

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

<h2>Solution</h2>

```python
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return repr(self.val)

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.filled = 0
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        if self.filled >= self.size:
            return False
        if self.filled == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newnode = Node(value)
            self.tail.next = newnode
            self.tail = newnode
        self.filled+=1
        return True

    def deQueue(self) -> bool:
        if self.filled <= 0:
            return False
        self.head = self.head.next
        self.filled -= 1
        return True

    def Front(self) -> int:
        if self.filled <= 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.filled <= 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.filled == 0

    def isFull(self) -> bool:
        return self.filled == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```
