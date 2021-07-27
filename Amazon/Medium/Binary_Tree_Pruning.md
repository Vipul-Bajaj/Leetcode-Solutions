# [Home](./../..)/[Amazon](./..)/[Medium](./)/Binary_Tree_Pruning
<h1>Binary Tree Pruning</h1>

<p>
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
</p>
<p>
A subtree of a node node is node plus every node that is a descendant of node.
</p>

<b>Example 1:</b>

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png">

    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    
<b>Example 2:</b>

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png">

    Input: root = [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
    
<b>Example 3:</b>

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png">

    Input: root = [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 200].
- Node.val is either 0 or 1.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node:
            return
        if node and not node.left and not node.right and node.val == 0:
            return None
        node.left = self.dfs(node.left)
        node.right = self.dfs(node.right)
        
        if not node.left and not node.right and node.val == 0:
            return None
        
        return node
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)
```
