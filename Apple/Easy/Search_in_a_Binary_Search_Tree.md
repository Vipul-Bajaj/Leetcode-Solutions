# [Home](./../..)/[Apple](./..)/[Easy](./)/Search_in_a_Binary_Search_Tree
<h1>Search in a Binary Search Tree</h1>

<p>
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg">

    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg">

    Input: root = [4,2,7,1,3], val = 5
    Output: []

<b>Constraints:</b>

- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val!=val:
            root = root.left if val<root.val else root.right
        
        return root
```
