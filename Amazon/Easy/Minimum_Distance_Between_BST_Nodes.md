# [Home](./../..)/[Amazon](./..)/[Easy](./)/Minimum_Distance_Between_BST_Nodes
<h1>Minimum Distance Between BST Nodes</h1>

<p>
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg">

    Input: root = [4,2,6,1,3]
    Output: 1
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg">

    Input: root = [1,0,48,null,null,12,49]
    Output: 1

<b>Constraints:</b>

- The number of nodes in the tree is in the range [2, 100].
- 0 <= Node.val <= 105

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = float('-inf')
        self.ans = float('inf')
        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            self.ans = min(self.ans, node.val-self.prev)
            self.prev = node.val
            inorderTraversal(node.right)
        
        inorderTraversal(root)
        return self.ans
```
