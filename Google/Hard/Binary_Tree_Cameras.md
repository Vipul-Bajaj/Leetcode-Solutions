# [Home](./../..)/[Google](./..)/[Hard](./)/Binary_Tree_Cameras
<h1>Binary Tree Cameras</h1>

<p>
Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png">

    Input: [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png">

    Input: [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

<b>Constraints:</b>

- The number of nodes in the given tree will be in the range [1, 1000].
- Every node has value 0.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,par):
        if not node:
            return
        
        self.dfs(node.left,node)
        self.dfs(node.right,node)
        
        if node.left not in self.visited or node.right not in self.visited or (par is None and node not in self.visited):
            self.ans+=1
            self.visited.update([node,par,node.left,node.right])
    def minCameraCover(self, root: TreeNode) -> int:
        self.visited = set([None])
        self.ans = 0
        self.dfs(root,None)
        return self.ans
```
