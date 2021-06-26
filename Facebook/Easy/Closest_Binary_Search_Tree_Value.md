# [Home](./../..)/[Facebook](./..)/[Easy](./)/Closest_Binary_Search_Tree_Value
<h1>Closest Binary Search Tree Value</h1>

<p>
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg">

    Input: root = [4,2,5,1,3], target = 3.714286
    Output: 4
    
<b>Example 2:</b>

    Input: root = [1], target = 4.428571
    Output: 1

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- 0 <= Node.val <= 109
- -109 <= target <= 109

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = None
        diff = 2**31-1
        st = [root]
        while st:
            node = st.pop()
            if abs(target-node.val)<diff:
                closest = node.val
                diff = abs(target-node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return closest
```
