# [Home](./../..)/[Facebook](./..)/[Medium](./)/Binary_Tree_Vertical_Order_Traversal
<h1>Binary Tree Vertical Order Traversal</h1>

<p>
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/28/vtree1.jpg">

    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/28/vtree2-1.jpg">

    Input: root = [3,9,8,4,0,1,7]
    Output: [[4],[9],[3,0,1],[8],[7]]
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/28/vtree2.jpg">

    Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
    Output: [[4],[9,5],[3,0,1],[8,2],[7]]
    
<b>Example 4:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 100].
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
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root,0)])
        hm = defaultdict(list)
        while q:
            node,col = q.popleft()
            hm[col].append(node.val)
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        
        res = []
        for k in sorted(hm.keys()):
            res.append(hm[k])
        return res
```
