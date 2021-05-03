# [Home](./../..)/[Facebook](./..)/[Medium](./)/Range_Sum_of_BST
<h1>Range Sum of BST</h1>

<p>
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg">

    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg">

    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    
<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 2 * 104].
- 1 <= Node.val <= 105
- 1 <= low <= high <= 105
- All Node.val are unique.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = [root]
        s= 0
        while q:
            u = q.pop(0)
            if low<=u.val<=high:
                s+=u.val
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        return s
```
