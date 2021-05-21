# [Home](./../..)/[Amazon](./..)/[Easy](./)/Binary_Tree_Preorder_Traversal
<h1>Binary Tree Preorder Traversal</h1>

<p>
Given the root of a binary tree, return the preorder traversal of its nodes' values.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg">

    Input: root = [1,null,2,3]
    Output: [1,2,3]
    
<b>Example 2:</b>
  
<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg">  

    Input: root = [1,2]
    Output: [1,2]

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg">
  
    Input: root = [1,null,2]
    Output: [1,2]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        st = [root]
        out = []
        while st:
            node = st.pop()
            out.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            
        return out
```
