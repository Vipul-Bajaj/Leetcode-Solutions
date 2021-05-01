<h1>Invert Binary Tree</h1>

<p>
Given the root of a binary tree, invert the tree, and return its root.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg">

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg">

    Input: root = [2,1,3]
    Output: [2,3,1]
    
<b>Example 3:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def mirror(node):
            if not node:
                return
            mirror(node.left)
            mirror(node.right)
            node.left,node.right = node.right,node.left
            
        mirror(root)
        return root
```
