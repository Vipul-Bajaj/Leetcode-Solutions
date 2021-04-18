<h1>Binary Tree Maximum Path Sum</h1>

<p>
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg">

    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg">

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 3 * 104].
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
    def maxSum(self,node,res):
        if not node:
            return 0
        l = self.maxSum(node.left,res)
        r = self.maxSum(node.right,res)
        
        max_now = max(max(l,r)+node.val,node.val)
        
        max_top = max(max_now,l+r+node.val)
        
        res[0] = max(res[0],max_top)
        
        return max_now
    
    def maxPathSum(self, root: TreeNode) -> int:
        res = [-2**31]
        
        self.maxSum(root,res)
        
        return res[0]
```
