# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Maximum_Width_of_Binary_Tree
<h1>Maximum Width of Binary Tree</h1>

<p>
Given the root of a binary tree, return the maximum width of the given tree.
</p>
<p>
The maximum width of a tree is the maximum width among all levels.
</p>
<p>
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.
</p>
<p>
It is guaranteed that the answer will in the range of 32-bit signed integer.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg">

    Input: root = [1,3,2,5,3,null,9]
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/width2-tree.jpg">

    Input: root = [1,3,null,5,3]
    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg">

    Input: root = [1,3,2,5]
    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).

<b>Example 4:</b>

<img src="https://assets.leetcode.com/uploads/2021/05/03/width4-tree.jpg">

    Input: root = [1,3,2,5,null,null,9,6,null,null,7]
    Output: 8
    Explanation: The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 3000].
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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root,0)])
        
        max_width = 0
        while q:
            level_length = len(q)
            _,level_head = q[0]
            for _ in range(level_length):
                node,col_idx = q.popleft()
                if node.left:
                    q.append((node.left,2*col_idx+1))
                if node.right:
                    q.append((node.right,2*col_idx+2))
            
            max_width = max(max_width,col_idx-level_head+1)
        return max_width
```
