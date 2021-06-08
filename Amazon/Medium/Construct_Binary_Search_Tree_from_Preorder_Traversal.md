# [Home](./../..)/[Amazon](./..)/[Medium](./)/Construct_Binary_Search_Tree_from_Preorder_Traversal
<h1>Construct Binary Search Tree from Preorder Traversal</h1>

<p>
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
</p>
<p>
It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
</p>
<p>
A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
</p>
<p>
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/03/06/1266.png">

    Input: preorder = [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]
    
<b>Example 2:</b>

    Input: preorder = [1,3]
    Output: [1,null,3]

<b>Constraints:</b>

- 1 <= preorder.length <= 100
- 1 <= preorder[i] <= 10^8
- All the values of preorder are unique.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        st = [root]
        for i in range(1,len(preorder)):
            node,child = st[-1],TreeNode(preorder[i])
            
            while st and st[-1].val<child.val:
                node = st.pop()
            
            if node.val<child.val:
                node.right = child
            else:
                node.left = child
            st.append(child)
        
        return root
```
