# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Trim_a_Binary_Search_Tree
<h1>Trim a Binary Search Tree</h1>

<p>
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
</p>
<p>
Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg">

    Input: root = [1,0,2], low = 1, high = 2
    Output: [1,null,2]

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg">

    Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
    Output: [3,2,null,1]

<b>Example 3:</b>

    Input: root = [1], low = 1, high = 2
    Output: [1]

<b>Example 4:</b>

    Input: root = [1,null,2], low = 1, high = 3
    Output: [1,null,2]

<b>Example 5:</b>

    Input: root = [1,null,2], low = 2, high = 4
    Output: [2]

<b>Constraints:</b>

- The number of nodes in the tree in the range [1, 104].
- 0 <= Node.val <= 104
- The value of each node in the tree is unique.
- root is guaranteed to be a valid binary search tree.
- 0 <= low <= high <= 10

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,low,high):
        if not node:
            return None
        if node.val>=low and node.val<=high:
            node.left = self.dfs(node.left,low,high)
            node.right = self.dfs(node.right,low,high)
            return node
        elif node.val<low:
            return self.dfs(node.right,low,high)
        else:
            return self.dfs(node.left,low,high)
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.dfs(root,low,high)
```
