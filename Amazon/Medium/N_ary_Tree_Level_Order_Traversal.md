# [Home](./../..)/[Amazon](./..)/[Medium](./)/N_ary_Tree_Level_Order_Traversal
<h1>N-ary Tree Level Order Traversal</h1>

<p>
Given an n-ary tree, return the level order traversal of its nodes' values.
</p>
<p>
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png">

    Input: root = [1,null,3,2,4,null,5,6]
    Output: [[1],[3,2,4],[5,6]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png">

    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
    
<b>Constraints:</b>

- The height of the n-ary tree is less than or equal to 1000
- The total number of nodes is between [0, 104]

<h2>Solution</h2>

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        traversal = []
        if not root:
            return []
        q = deque([root,None])
        level = []
        while q:
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.children:
                    q.extend(node.children)
            else:
                traversal.append(level)
                level = []
                if q:
                    q.append(None)
        return traversal
```
