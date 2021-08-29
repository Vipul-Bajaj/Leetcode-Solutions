# [Home](./../..)/[Amazon](./..)/[Medium](./)/Equal_Tree_Partition
<h1>Equal Tree Partition</h1>

<p>
Given the root of a binary tree, return true if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/split1-tree.jpg">

    Input: root = [5,10,10,null,null,2,3]
    Output: true

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/split2-tree.jpg">

    Input: root = [1,2,10,null,null,2,20]
    Output: false
    Explanation: You cannot split the tree into two trees with equal sums after removing exactly one edge on the tree.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 105

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        seen = []
        
        def dfs(node):
            if not node:
                return 0
            seen.append(dfs(node.left)+dfs(node.right)+node.val)
            return seen[-1]
        
        total = dfs(root)
        seen.pop()
        return (total/2) in seen
```
