# [Home](./../..)/[Facebook](./..)/[Medium](./)/Flatten_Nested_List_Iterator
<h1>Flatten Nested List Iterator</h1>

<p>
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

</p>

<b>Example 1:</b>

    Input: nestedList = [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
    
<b>Example 2:</b>

    Input: nestedList = [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

<b>Constraints:</b>

- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-106, 106].

<h2>Solution</h2>

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def _flatten(self,nestedlist):
        for nestedinteger in nestedlist:
            if nestedinteger.isInteger():
                self.flatten_list.append(nestedinteger.getInteger())
            else:
                self._flatten(nestedinteger.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = []
        self._flatten(nestedList)
        self.count = 0
        self.size = len(self.flatten_list)
    
    def next(self) -> int:
        value = self.flatten_list[self.count]
        self.count+=1
        return value
    
    def hasNext(self) -> bool:
         return self.count < self.size

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```
