# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal
# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal
<h1>Construct Binary Tree from Inorder and Postorder Traversal</h1>

<p>
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg">

    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
    
<b>Example 2:</b>

    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

<b>Constraints:</b>

- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of unique values.
- Each value of postorder also appears in inorder.
- inorder is guaranteed to be the inorder traversal of the tree.
- postorder is guaranteed to be the postorder traversal of the tree.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generate(self,postorder,start,end):
        if start>end:
            return
        node = TreeNode(postorder[self.preorder_idx])
        idx = self.hm[node.val]
        self.preorder_idx-=1
        if start == end:
            return node
        node.right = self.generate(postorder,idx+1,end)
        node.left = self.generate(postorder,start,idx-1)
        return node
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.hm = {}
        n = len(postorder)
        self.preorder_idx = n-1
        for i in range(n):
            self.hm[inorder[i]] = i
        return self.generate(postorder,0,n-1)
```
