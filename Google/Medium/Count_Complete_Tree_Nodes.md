# [Home](./../..)/[Google](./..)/[Medium](./)/Count_Complete_Tree_Nodes
<h1>Count Complete Tree Nodes</h1>

<p>
Given the root of a complete binary tree, return the number of the nodes in the tree.
</p>
<p>
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
</p>
<p>
Design an algorithm that runs in less than O(n) time complexity.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg">

    Input: root = [1,2,3,4,5,6]
    Output: 6
 
<b>Example 2:</b>

    Input: root = []
    Output: 0

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 5 * 104].
- 0 <= Node.val <= 5 * 104
- The tree is guaranteed to be complete.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exists(self,idx,d,node):
        left ,right = 0,2**d-1
        for _ in range(d):
            mid = (left+right)//2
            if idx<=mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid+1
        return node is not None
    def countNodes(self, root: TreeNode) -> int:
        d = 0
        if not root:
            return 0
        node = root
        while node.left:
            node = node.left
            d+=1
        if d == 0:
            return 1
        
        left ,right = 1,2**d-1
        while left<=right:
            mid = (left+right)//2
            if self.exists(mid,d,root):
                left = mid+1
            else:
                right = mid-1
        
        return (2**d - 1) + left
```
