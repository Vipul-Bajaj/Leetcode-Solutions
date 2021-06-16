# [Home](./../..)/[Box](./..)/[Easy](./)/Univalued_Binary_Tree
<h1>Univalued Binary Tree</h1>

<p>
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png">

    Input: [1,1,1,1,1,null,1]
    Output: true
  
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png">

    Input: [2,2,2,5,2]
    Output: false
    
<b>Constraints:</b>

- The number of nodes in the given tree will be in the range [1, 100].
- Each node's value will be an integer in the range [0, 99].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        st = [root]
        while st:
            node = st.pop()
            
            if node.val != val:
                return False
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            
        return True
```
