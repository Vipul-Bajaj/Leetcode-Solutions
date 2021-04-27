<h1>Binary Tree Level Order Traversal</h1>

<p>
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg">

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    
<b>Example 2:</b>

    Input: root = [1]
    Output: [[1]]
    
<b>Example 3:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 2000].
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root,None])
        level= []
        while q:
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                ans.append(level)
                level = []
                if q:
                    q.append(None)
        return ans
```
