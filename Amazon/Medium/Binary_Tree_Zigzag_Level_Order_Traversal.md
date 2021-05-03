# [Home](./../..)/[Amazon](./..)/[Medium](./)/Binary_Tree_Zigzag_Level_Order_Traversal
<h1>Binary Tree Zigzag Level Order Traversal</h1>

<p>
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg">

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]
    
<b>Example 2:</b>

    Input: root = [1]
    Output: [[1]]
    
<b>Example 3:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 2000].
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        st1 = [root] if root else []
        st2 = []
        ans = []
        while st1 or st2:
            curr = []
            while st1:
                node = st1.pop()
                curr.append(node.val)
                if node.left:
                    st2.append(node.left)
                if node.right:
                    st2.append(node.right)
            if curr:
                ans.append(curr)
            curr = []
            while st2:
                node = st2.pop()
                curr.append(node.val)
                if node.right:
                    st1.append(node.right)
                if node.left:
                    st1.append(node.left)
            if curr:
                ans.append(curr)
        return ans
```
