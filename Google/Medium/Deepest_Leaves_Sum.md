<h1>Deepest Leaves Sum</h1>

<p>
Given the root of a binary tree, return the sum of values of its deepest leaves.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png">

    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15
    
<b>Example 2:</b>

    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 19

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- 1 <= Node.val <= 100

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        q.append(None)
        l = []
        s = 0
        while q:
            node = q.popleft()
            if node:
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            else:
                if q:
                    q.append(None)
                s = sum(l)
                l = []
        return s
```
