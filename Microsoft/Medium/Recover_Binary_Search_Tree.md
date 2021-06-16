# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Recover_Binary_Search_Tree
<h1>Recover Binary Search Tree</h1>

<p>
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
</p>
<p>
Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg">

    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
    Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg">

    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]
    Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [2, 1000].
- -231 <= Node.val <= 231 - 1

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred 
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val
```
