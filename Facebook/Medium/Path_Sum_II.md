# [Home](./../..)/[Facebook](./..)/[Medium](./)/Path_Sum_II
<h1>Path Sum II</h1>

<p>
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg">

    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg">

    Input: root = [1,2,3], targetSum = 5
    Output: []

<b>Example 3:</b>

    Input: root = [1,2], targetSum = 0
    Output: []

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
    def hasSumPath(self,node,currSum,target,ans,path):
        if not node:
            return False
        if node and node.left is None and node.right is None:
            if target == currSum+node.val:
                ans.append((path + [node.val]).copy())
            return False
        currSum+=node.val
        if node.left:
            self.hasSumPath(node.left,currSum,target,ans,path + [node.val])
        if node.right:
            self.hasSumPath(node.right,currSum,target,ans,path + [node.val])
        return ans
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.hasSumPath(root,0,targetSum,res,[])
        return res
```
