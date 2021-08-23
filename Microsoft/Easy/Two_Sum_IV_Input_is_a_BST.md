# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Two_Sum_IV_Input_is_a_BST
<h1>Two Sum IV - Input is a BST</h1>

<p>
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg">

    Input: root = [5,3,6,2,4,null,7], k = 9
    Output: true

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg">

    Input: root = [5,3,6,2,4,null,7], k = 28
    Output: false

<b>Example 3:</b>

    Input: root = [2,1,3], k = 4
    Output: true

<b>Example 4:</b>

    Input: root = [2,1,3], k = 1
    Output: false

<b>Example 5:</b>

    Input: root = [2,1,3], k = 3
    Output: true
<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -104 <= Node.val <= 104
- root is guaranteed to be a valid binary search tree.
- -105 <= k <= 105

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,k):
        if not node:
            return False
        if k-node.val in self.s:
            return True
        else:
            self.s[node.val] = 1
            return self.dfs(node.left,k) or self.dfs(node.right,k)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.s = {}
        return self.dfs(root,k)
```
