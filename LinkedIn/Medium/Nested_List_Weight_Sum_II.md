# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Nested_List_Weight_Sum_II
<h1>Nested List Weight Sum II</h1>

<p>
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex1.png">

    Input: nestedList = [[1,1],2,[1,1]]
    Output: 8
    Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
    1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex2.png">

    Input: nestedList = [1,[4,[6]]]
    Output: 17
    Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
    1*3 + 4*2 + 6*1 = 17

<b>Constraints:</b>

- 1 <= nestedList.length <= 50
- The values of the integers in the nested list is in the range [-100, 100].
- The maximum depth of any integer is less than or equal to 50.

<h2>Solution</h2>

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        flatten_list = []
        max_depth = [1]
        def flatten(nestedlist,depth,flatten_list,max_depth):
            for nestedinteger in nestedlist:
                if nestedinteger.isInteger():
                    max_depth[0] = max(max_depth[0],depth)
                    flatten_list.append((nestedinteger.getInteger(),depth))
                else:
                    flatten(nestedinteger.getList(),depth+1,flatten_list,max_depth)
        s = 0
        flatten(nestedList,1,flatten_list,max_depth)
        for ele in flatten_list:
            s += (max_depth[0]-ele[1]+1)*ele[0]
        return s
```
