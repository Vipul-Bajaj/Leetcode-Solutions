# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal
# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal
<h1>Construct Binary Tree from Preorder and Inorder Traversal</h1>

<p>
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg">

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    
<b>Example 2:</b>

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

<b>Constraints:</b>

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generate(self,preorder,start,end):
        if start>end:
            return
        node = TreeNode(preorder[self.preorder_idx])
        idx = self.hm[node.val]
        self.preorder_idx+=1
        if start == end:
            return node
        node.left = self.generate(preorder,start,idx-1)
        node.right = self.generate(preorder,idx+1,end)
        return node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.hm = {}
        n = len(preorder)
        self.preorder_idx = 0
        for i in range(n):
            self.hm[inorder[i]] = i
        return self.generate(preorder,0,n-1)
```
