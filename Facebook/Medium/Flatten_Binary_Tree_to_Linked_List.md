# [Home](./../..)/[Facebook](./..)/[Medium](./)/Flatten_Binary_Tree_to_Linked_List
<h1>Flatten Binary Tree to Linked List</h1>

<p>
Given the root of a binary tree, flatten the tree into a "linked list":
</p>

* The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
* The "linked list" should be in the same order as a pre-order traversal of the binary tree.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg">

    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

<b>Example 2:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 2000].
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
```
