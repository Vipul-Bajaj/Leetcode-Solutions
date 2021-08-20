# [Home](./../..)/[Gilt Groupe](./..)/[Medium](./)/Add_One_Row_to_Tree
<h1>Add One Row to Tree</h1>

<p>
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
</p>
<p>
Note that the root node is at depth 1.
</p>
<p>
The adding rule is:
</p>

- Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
- cur's original left subtree should be the left subtree of the new left subtree root.
- cur's original right subtree should be the right subtree of the new right subtree root.
- If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg">

    Input: root = [4,2,6,3,1,5], val = 1, depth = 2
    Output: [4,1,1,2,null,null,6,3,1,5]

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg">

    Input: root = [4,2,null,3,1], val = 1, depth = 3
    Output: [4,2,null,1,1,3,null,null,1]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- The depth of the tree is in the range [1, 104].
- -100 <= Node.val <= 100
- -105 <= val <= 105
- 1 <= depth <= the depth of tree + 1

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,depth,req_depth,val):
        if not node:
            return
        if depth+1 == req_depth:
            node.left = TreeNode(val,left=node.left)
            node.right = TreeNode(val,None,right=node.right)
        else:
            self.dfs(node.left,depth+1,req_depth,val)
            self.dfs(node.right,depth+1,req_depth,val)
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val,left=root)
            return root
        self.dfs(root,1,depth,val)
        return root
```
