# [Home](./../..)/[Amazon](./..)/[Medium](./)/Maximum_Product_of_Splitted_Binary_Tree
<h1>Maximum Product of Splitted Binary Tree</h1>

<p>
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
</p>
<p>
Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
</p>
<p>
Note that you need to maximize the answer before taking the mod and not after taking it.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png">

    Input: root = [1,2,3,4,5,6]
    Output: 110
    Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png">

    Input: root = [1,null,2,3,4,null,null,5,6]
    Output: 90
    Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

<b>Example 3:</b>

    Input: root = [2,3,9,10,7,8,6,5,4,11,1]
    Output: 1025

<b>Example 4:</b>

    Input: root = [1,1]
    Output: 1

<b>Constraints:</b>

- The number of nodes in the tree is in the range [2, 5 * 104].
- 1 <= Node.val <= 104

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getTreeSum(self,node):
        s=node.val
        if node.left:
            s+=self.getTreeSum(node.left)
        if node.right:
            s+=self.getTreeSum(node.right)
        self.sum[node]=s
        return s
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sum = {}
        ts = self.getTreeSum(root)
        max_sum = 0
        for s in self.sum.values():
            max_sum = max(max_sum,(ts-s)*s)
        return max_sum%((10**9)+7)
```
