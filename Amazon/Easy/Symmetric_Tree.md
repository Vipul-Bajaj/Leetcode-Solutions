# [Home](./../..)/[Amazon](./..)/[Easy](./)/Symmetric_Tree
<h1>Symmetric Tree</h1>

<p>
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg">

    Input: root = [1,2,2,3,4,4,3]
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg">

    Input: root = [1,2,2,null,3,null,3]
    Output: false

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 1000].
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
    def checkSymmetry(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val==root2.val and self.checkSymmetry(root1.left,root2.right) and self.checkSymmetry(root1.right,root2.left))
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkSymmetry(root.left,root.right)
```
