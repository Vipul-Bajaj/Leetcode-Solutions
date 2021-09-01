# [Home](./../..)/[Amazon](./..)/[Medium](./)/Maximum_Average_Subtree
<h1>Maximum Average Subtree</h1>

<p>
Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.
</p>
<p>
A subtree of a tree is any node of that tree plus all its descendants.
</p>
<p>
The average value of a tree is the sum of its values, divided by the number of nodes.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/04/09/1308_example_1.png">

    Input: root = [5,6,1]
    Output: 6.00000
    Explanation: 
    For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
    For the node with value = 6 we have an average of 6 / 1 = 6.
    For the node with value = 1 we have an average of 1 / 1 = 1.
    So the answer is 6 which is the maximum.

<b>Example 2:</b>

    Input: root = [0,null,1]
    Output: 1.00000

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- 0 <= Node.val <= 105

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,max_avg):
        if not node:
            return 0,0
        left,lc = self.dfs(node.left,max_avg)
        right,rc = self.dfs(node.right,max_avg)
        tc= lc+rc+1
        s = (left+right+node.val)
        max_avg[0] = max(max_avg[0],s/tc)
        return s,tc
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = [0]
        self.dfs(root,max_avg)
        return max_avg[0]
```
