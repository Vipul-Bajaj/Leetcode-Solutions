# [Home](./../..)/[Google](./..)/[Medium](./)/Delete_Nodes_And_Return_Forest
<h1>Delete Nodes And Return Forest</h1>

<p>
Given the root of a binary tree, each node in the tree has a distinct value.
</p>
<p>
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
</p>
<p>
Return the roots of the trees in the remaining forest. You may return the result in any order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png">

    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]
    
<b>Example 2:</b>

    Input: root = [1,2,4,null,3], to_delete = [3]
    Output: [[1,2,4]]

<b>Constraints:</b>

- The number of nodes in the given tree is at most 1000.
- Each node has a distinct value between 1 and 1000.
- to_delete.length <= 1000
- to_delete contains distinct values between 1 and 1000.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        res = []
        def delete(node, is_root):
            if not node:
                return None
            root_deleted = node.val in delete_set
            if is_root and not root_deleted:
                res.append(node)
            node.left = delete(node.left,root_deleted)
            node.right = delete(node.right,root_deleted)
            return None if root_deleted else node
        delete(root,True)
        return res
```
