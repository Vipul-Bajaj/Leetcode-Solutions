<h1>Path Sum</h1>

<p>
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg">

    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg">

    Input: root = [1,2,3], targetSum = 5
    Output: false
    
<b>Example 3:</b>

    Input: root = [1,2], targetSum = 0
    Output: false

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSumPath(self,node,currSum,target):
        if not node:
            return False
        if node and node.left is None and node.right is None:
            if target == currSum+node.val:
                return True
            return False
        currSum+=node.val
        ans = False
        if node.left:
            ans = self.hasSumPath(node.left,currSum,target) or ans
        if not ans and node.right:
            ans = self.hasSumPath(node.right,currSum,target) or ans
        return ans    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.hasSumPath(root,0,targetSum)
```
