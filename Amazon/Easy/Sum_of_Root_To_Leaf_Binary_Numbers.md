# [Home](./../..)/[Amazon](./..)/[Easy](./)/Sum_of_Root_To_Leaf_Binary_Numbers
<h1>Sum of Root To Leaf Binary Numbers</h1>

<p>
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
</p>
<p>
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
</p>
<p>
Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.
</p>

<b>Example 1:</b>

    Input: root = [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
    
<b>Example 2:</b>

    Input: root = [0]
    Output: 0

<b>Example 3:</b>

    Input: root = [1]
    Output: 1
    
<b>Example 4:</b>
    
    Input: root = [1,1]
    Output: 3

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 1000].
- Node.val is 0 or 1.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySum(self,node,path,s):
        if not node:
            return
        if node and not node.left and not node.right:
            s[0]+=int("".join(path)+str(node.val),2)
        if node.left:
            self.binarySum(node.left,path+[str(node.val)],s)
        if node.right:
            self.binarySum(node.right,path+[str(node.val)],s)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        s = [0]
        self.binarySum(root,[],s)
        return s[0]
```
