# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Validate_Binary_Search_Tree
<h1>Validate Binary Search Tree</h1>

<p>
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg">

    Input: root = [2,1,3]
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg">

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        st = [(root,-math.inf,math.inf)]
        while st:
            node,lower_limit,upper_limit = st.pop()
            if not node:
                continue
            val = node.val
            if val<=lower_limit or val>=upper_limit:
                return False
            st.append((node.right,val,upper_limit))
            st.append((node.left,lower_limit,val))
        return True
        return anagrams.values()
```
