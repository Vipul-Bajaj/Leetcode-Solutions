# [Home](./../..)/[Facebook](./..)/[Easy](./)/Diameter_of_Binary_Tree
<h1>Diameter of Binary Tree</h1>

<p>
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg">

    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
    
<b>Example 2:</b>

    Input: root = [1,2]
    Output: 1

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
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
    def longestPath(self,node):
        if not node:
            return 0
        left = self.longestPath(node.left)
        right = self.longestPath(node.right)
        self.diameter = max(self.diameter,left+right)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.longestPath(root)
        return self.diameter
```
