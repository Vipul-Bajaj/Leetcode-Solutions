# [Home](./../..)/[Apple](./..)/[Medium](./)/Binary_Tree_Level_Order_Traversal_II
<h1>Binary Tree Level Order Traversal II</h1>

<p>
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg">

    Input: root = [3,9,20,null,null,15,7]
    Output: [[15,7],[9,20],[3]]
    
<b>Example 2:</b>

    Input: root = [1]
    Output: [[1]]

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root,None])
        ans = []
        l = []
        while q:
            node = q.popleft()
            if not node:
                ans.append(l)
                l = []
                if q:
                    q.append(None)
            else:
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        # ans = []
        # for k in sorted(hm,reverse=True):
        #     ans.append(hm[k])
        return ans[::-1]
```
