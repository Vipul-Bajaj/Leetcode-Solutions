# [Home](./../..)/[Amazon](./..)/[Easy](./)/Cousins_in_Binary_Tree
<h1>Cousins in Binary Tree</h1>

<p>
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
</p>
<p>
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
</p>
<p>
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
</p>
<p>
Return true if and only if the nodes corresponding to the values x and y are cousins.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png">

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false
    
<b>Example 2:</b>
  
<img src="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png">  

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png">
  
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

<b>Constraints:</b>

- The number of nodes in the tree will be between 2 and 100.
- Each node has a unique integer value from 1 to 100.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        hm = {}
        
        def dfs(node,par,depth):
            if not node:
                return
            hm[node.val] = [par,depth]
            if node.left:
                dfs(node.left,node.val,depth+1)
            if node.right:
                dfs(node.right,node.val,depth+1)
        
        dfs(root,None,0)
        
        return hm[x][0]!=hm[y][0] and hm[x][1]==hm[y][1]
```
