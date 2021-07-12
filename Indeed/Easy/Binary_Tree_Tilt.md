# [Home](./../..)/[Indeed](./..)/[Easy](./)/Binary_Tree_Tilt
<h1>Binary Tree Tilt</h1>

<p>
Given the root of a binary tree, return the sum of every tree node's tilt.
</p>
<p>
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg">

    Input: root = [1,2,3]
    Output: 1
    Explanation: 
    Tilt of node 2 : |0-0| = 0 (no children)
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
    Sum of every tilt : 0 + 0 + 1 = 1
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg">

    Input: root = [4,2,9,3,5,null,7]
    Output: 15
    Explanation: 
    Tilt of node 3 : |0-0| = 0 (no children)
    Tilt of node 5 : |0-0| = 0 (no children)
    Tilt of node 7 : |0-0| = 0 (no children)
    Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
    Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
    Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
    Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg">

    Input: root = [21,7,14,1,1,2,2,3,3]
    Output: 9

<b>Constraint:</b>
- The number of nodes in the tree is in the range [0, 104].
- -1000 <= Node.val <= 1000

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,s):
        if not node:
            return 0
        left = self.dfs(node.left,s)
        right = self.dfs(node.right,s)
        s[0]+=abs(left-right)
        return left+right+node.val
    def findTilt(self, root: TreeNode) -> int:
        s = [0]
        self.dfs(root,s)
        return s[0]
```
