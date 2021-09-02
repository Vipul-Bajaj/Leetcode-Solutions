# [Home](./../..)/[Amazon](./..)/[Easy](./)/Subtree_of_Another_Tree
<h1>Subtree of Another Tree</h1>

<p>
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
</p>
<p>
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg">

    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg">

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

<b>Constraints:</b>

- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -104 <= root.val <= 104
- -104 <= subRoot.val <= 104

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
#         def isSimilar(root1,root2):
#             if not root1 and not root2:
#                 return True
#             if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
#                 return False
#             return isSimilar(root1.left,root2.left) and isSimilar(root1.right,root2.right)
        
#         q = deque([root])
        
#         while q:
#             node = q.popleft()
#             if node.val == subRoot.val and isSimilar(node, subRoot):
#                 return True
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         return False
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def preorder(node,isLeft):
            if not node:
                return "lNull" if isLeft else "rNull"
            return " "+str(node.val)+" "+preorder(node.left,True)+" "+preorder(node.right,False)
        return preorder(subRoot, True) in preorder(root, True)
```
