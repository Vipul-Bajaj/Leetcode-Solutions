# [Home](./../..)/[Google](./..)/[Medium](./)/Flip_Equivalent_Binary_Trees
<h1>Flip Equivalent Binary Trees</h1>

<p>
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
</p>
<p>
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
</p>
<p>
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png">

    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
 
<b>Example 2:</b>

    Input: root1 = [], root2 = []
    Output: true

<b>Example 3:</b>

    Input: root1 = [0,null,1], root2 = []
    Output: false
    
<b>Constraints:</b>

- The number of nodes in each tree is in the range [0, 100].
- Each tree will have unique node values in the range [0, 99].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
```
