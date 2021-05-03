# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Binary_Tree_Right_Side_View
<h1>Binary Tree Right Side View</h1>

<p>
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg">

    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    
<b>Example 2:</b>

    Input: root = [1,null,3]
    Output: [1,3]
    
<b>Example 3:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

<h2>Solution</h2>

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = deque()
        q = deque()
        q.append(root)
        
        while q:
            n = len(q)
            for i in range(1,n+1):
                ele = q.popleft()
                if i == n:
                    res.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        
        return res
```
