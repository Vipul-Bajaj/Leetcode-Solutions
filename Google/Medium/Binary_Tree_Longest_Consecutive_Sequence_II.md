# [Home](./../..)/[Google](./..)/[Medium](./)/Binary_Tree_Longest_Consecutive_Sequence_II
<h1>Binary Tree Longest Consecutive Sequence II</h1>

<p>
Given the root of a binary tree, return the length of the longest consecutive path in the tree.
</p>
<p>
This path can be either increasing or decreasing.
</p>

- For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.

<p>
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/14/consec2-1-tree.jpg">

    Input: root = [1,2,3]
    Output: 2
    Explanation: The longest consecutive path is [1, 2] or [2, 1].
    
<b>Example 2:</b>    

<img src="https://assets.leetcode.com/uploads/2021/03/14/consec2-2-tree.jpg">

    Input: root = [2,1,3]
    Output: 3
    Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

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
    def longestConsecutive(self, root: TreeNode) -> int:
        maxval = 0
        def longest_path(root):
            nonlocal maxval
            if not root:
                return [0,0]
            
            inr=dcr = 1
            if root.left:
                left = longest_path(root.left)
                if root.val == root.left.val+1:
                    dcr = left[1]+1
                elif root.val == root.left.val-1:
                    inr = left[0]+1
            if root.right:
                right = longest_path(root.right)
                if (root.val == root.right.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    inr = max(inr, right[0] + 1)
            maxval = max(maxval,dcr+inr-1)
            return [inr,dcr]
        
        longest_path(root)
        return maxval
```
