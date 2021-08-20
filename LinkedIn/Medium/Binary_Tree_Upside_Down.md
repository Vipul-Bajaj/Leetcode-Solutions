# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Binary_Tree_Upside_Down
<h1>Binary Tree Upside Down</h1>

<p>
Given the root of a binary tree, turn the tree upside down and return the new root.
</p>
<p>
You can turn a binary tree upside down with the following steps:
</p>

- The original left child becomes the new root.
- The original root becomes the new right child.
- The original right child becomes the new left child.

<p>
<img src="https://assets.leetcode.com/uploads/2020/08/29/main.jpg">
  
The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/08/29/updown.jpg">

    Input: root = [1,2,3,4,5]
    Output: [4,5,2,null,null,3,1]

<b>Example 2:</b>

    Input: root = []
    Output: []

<b>Example 3:</b>

    Input: root = [1]
    Output: [1]

<b>Constraints:</b>

- The number of nodes in the tree will be in the range [0, 10].
- 1 <= Node.val <= 10
- Every right node in the tree has a sibling (a left node that shares the same parent).

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        
        return left
```
