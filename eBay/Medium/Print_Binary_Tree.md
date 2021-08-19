# [Home](./../..)/[eBay](./..)/[Medium](./)/Print_Binary_Tree
<h1>Print Binary Tree</h1>

<p>
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:
</p>

- The height of the tree is height and the number of rows m should be equal to height + 1.
- The number of columns n should be equal to 2height+1 - 1.
- Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
- For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
- Continue this process until all the nodes in the tree have been placed.
- Any empty cells should contain the empty string "".

<p>
Return the constructed matrix res.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg">

    Input: root = [1,2]
    Output: 
    [["","1",""],
     ["2","",""]]

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg">

    Input: root = [1,2,3,null,4]
    Output: 
    [["","","","1","","",""],
     ["","2","","","","3",""],
     ["","","4","","","",""]]
    
<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 210].
- -99 <= Node.val <= 99
- The depth of the tree will be in the range [1, 10].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,node):
        if not node:
            return 0
        lHeight = self.getHeight(node.left)
        rHeight = self.getHeight(node.right)
        return max(lHeight,rHeight)+1
    
    def dfs(self,node,r,c,height,mat):
        if not node:
            return
        if node.left:
            nr,nc = r+1,c-2**(height-r-2)
            mat[nr][nc] = str(node.left.val)
            self.dfs(node.left,nr,nc,height,mat)
        if node.right:
            nr,nc = r+1,c+2**(height-r-2)
            mat[nr][nc] = str(node.right.val)
            self.dfs(node.right,nr,nc,height,mat)
    
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.getHeight(root)
        m,n = height,(2**height)-1
        mat = [["" for j in range(n)]for i in range(m)]
        mat[0][(n-1)//2] = str(root.val)
        self.dfs(root,0,(n-1)//2,height,mat)
        return mat
```
