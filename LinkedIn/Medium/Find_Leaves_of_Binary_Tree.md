# [Home](./../..)/[LinkedIn](./..)/[Medium](./)/Find_Leaves_of_Binary_Tree
<h1>Find Leaves of Binary Tree</h1>

<p>
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
</p>

- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/16/remleaves-tree.jpg">

    Input: root = [1,2,3,4,5]
    Output: [[4,5,3],[2],[1]]
    Explanation:
    [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
    
<b>Example 2:</b>

    Input: root = [1]
    Output: [[1]]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # O(h^2) Solution
# class Solution:
#     def findLeaves(self, root: TreeNode) -> List[List[int]]:
#         out = []
#         def dfs(node,l):
#             if not node:
#                 return False
#             if not node.right and not node.left:
#                 l.append(node.val)
#                 return True
#             left = dfs(node.left,l)
#             right = dfs(node.right,l)
#             if left:
#                 node.left = None
#             if right:
#                 node.right = None
#             return False
#         leaves = []
#         while not dfs(root,leaves):
#             out.append(leaves)
#             leaves = []
#         out.append([root.val])
#         return out  

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res= []
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            level = max(left,right)+1
            if level == len(res)+1:
                res.append([])
            res[level-1].append(node.val)
            return level
        dfs(root)
        return res
```
