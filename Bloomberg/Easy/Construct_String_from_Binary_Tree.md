# [Home](./../..)/[Bloomberg](./..)/[Easy](./)/Construct_String_from_Binary_Tree
<h1>Construct String from Binary Tree</h1>

<p>
Given the root of a binary tree, construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way, and return it.
</p>
<p>
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg">

    Input: root = [1,2,3,4]
    Output: "1(2(4))(3)"
    Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg">

    Input: root = [1,2,3,null,4]
    Output: "1(2()(4))(3)"
    Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -1000 <= Node.val <= 1000

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(str(node.val))
            if node.left:
                ans.append('(')
                preorder(node.left)
                ans.append(')')
            elif not node.left and node.right:
                ans.append('(')
                ans.append(')')
            if node.right:
                ans.append('(')
                preorder(node.right)
                ans.append(')')
        
        preorder(root)
        return "".join(ans)
```
