# [Home](./../..)/[Facebook](./..)/[Medium](./)/Maximum_Level_Sum_of_a_Binary_Tree
<h1>Maximum Level Sum of a Binary Tree</h1>

<p>
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
<br>
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/05/03/capture.JPG">

    Input: root = [1,7,0,7,-8,null,null]
    Output: 2
    Explanation: 
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.

<b>Example 2:</b>

    Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    Output: 2

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 1054

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = root.val
        q = deque([root,None])
        ls = 0
        l = 1
        level = 1
        while q:
            node = q.popleft()
            if not node:
                if ls > max_sum:
                    level = l
                    max_sum = ls
                l+=1
                ls = 0
                if q:
                    q.append(None)
            else:
                ls+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level
```
