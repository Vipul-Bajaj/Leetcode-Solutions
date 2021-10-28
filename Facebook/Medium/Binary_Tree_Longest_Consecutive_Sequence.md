# [Home](./../..)/[Facebook](./..)/[Medium](./)/Binary_Tree_Longest_Consecutive_Sequence
<h1>Binary Tree Longest Consecutive Sequence</h1>

<p>
Given the root of a binary tree, return the length of the longest consecutive sequence path.
</p>
<p>
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/consec1-1-tree.jpg">

    Input: root = [1,null,3,2,4,null,null,null,5]
    Output: 3
    Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/consec1-2-tree.jpg">

    Input: root = [2,null,3,2,null,1]
    Output: 2
    Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 3 * 104].
- -3 * 104 <= Node.val <= 3 * 104

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node,parent, length):
            if not node:
                return length
            length = length+1 if parent and parent.val+1 == node.val else 1
            return max(length, dfs(node.left, node, length), dfs(node.right, node, length))
        
        return dfs(root, None, 0)
```
