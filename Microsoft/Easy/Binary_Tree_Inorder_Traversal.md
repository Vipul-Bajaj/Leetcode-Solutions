# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Binary_Tree_Inorder_Traversal
<h1>Binary Tree Inorder Traversal</h1>

<p>
Given the root of a binary tree, return the inorder traversal of its nodes' values.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg">

    Input: root = [1,null,2,3]
    Output: [1,3,2]

<b>Example 2:</b>

    Input: root = []
    Output: []

<b>Example 3:</b>

    Input: root = [1]
    Output: [1]


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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        arr = []
        while True:
            if root:
                st.append(root)
                root = root.left
            elif st:
                root = st.pop()
                arr.append(root.val)
                root = root.right
            else:
                break
        return arr
```
