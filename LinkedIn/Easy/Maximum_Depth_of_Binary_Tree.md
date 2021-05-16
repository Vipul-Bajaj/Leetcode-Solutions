# [Home](./../..)/[LinkedIn](./..)/[Easy](./)/Maximum_Depth_of_Binary_Tree
<h1>Maximum Depth of Binary Tree</h1>

<p>
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg">

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

<b>Example 2:</b>

    Input: root = [1,null,2]
    Output: 2

<b>Example 3:</b>

    Input: root = []
    Output: 0

<b>Example 4:</b>

    Input: root = [0]
    Output: 1
    
<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 104].
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
    def depth(self,node,depth,max_depth):
        if not node:
            return
        depth+=1
        max_depth[0] = max(depth,max_depth[0])
        self.depth(node.left,depth,max_depth)
        self.depth(node.right,depth,max_depth)
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        max_depth = [0]
        self.depth(root,depth,max_depth)
        return max_depth[0]
```
