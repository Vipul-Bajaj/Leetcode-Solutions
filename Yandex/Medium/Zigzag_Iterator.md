# [Home](./../..)/[Yandex](./..)/[Medium](./)/Zigzag_Iterator
<h1>Zigzag Iterator</h1>

<p>
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.
<br>
Implement the ZigzagIterator class:
</p>

* ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
* boolean hasNext() returns true if the iterator still has elements, and false otherwise.
* int next() returns the current element of the iterator and moves the iterator to the next element.

<b>Example 1:</b>

    Input: v1 = [1,2], v2 = [3,4,5,6]
    Output: [1,3,2,4,5,6]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
    
<b>Example 2:</b>

    Input: v1 = [1], v2 = []
    Output: [1]
  
<b>Example 3:</b>

    Input: v1 = [], v2 = [1]
    Output: [1]  
<b>Constraints:</b>

- 0 <= v1.length, v2.length <= 1000
- 1 <= v1.length + v2.length <= 2000
- -231 <= v1[i], v2[i] <= 231 - 1

<h2>Solution</h2>

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.count = 0
        self.total = len(v1)+len(v2)
        self.vec = [v1,v2]
        self.v1,self.v2 = 0,0
        self.n1,self.n2 = len(v1),len(v2)
        self.turn = 1 if self.n1>0 else 2

    def next(self) -> int:
        self.count+=1
        if self.turn == 1:
            ele = self.vec[0][self.v1]
            self.v1+=1
            if self.v2<self.n2:
                self.turn=2
            return ele
        ele = self.vec[1][self.v2]
        self.v2+=1
        if self.v1<self.n1:
            self.turn=1
        return ele
    def hasNext(self) -> bool:
        return self.count<self.total

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
```
