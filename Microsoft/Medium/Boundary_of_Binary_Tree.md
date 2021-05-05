# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Boundary_of_Binary_Tree
<h1>Boundary of Binary Tree</h1>

<p>
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

- The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
- If a node in the left boundary and has a left child, then the left child is in the left boundary.
- If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
- The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/11/boundary1.jpg">

    Input: root = [1,null,2,3,4]
    Output: [1,3,4,2]
    Explanation:
    - The left boundary is empty because the root does not have a left child.
    - The right boundary follows the path starting from the root's right child 2 -> 4.
      4 is a leaf, so the right boundary is [2].
    - The leaves from left to right are [3,4].
    Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/11/boundary2.jpg">

    Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
    Output: [1,2,4,7,8,9,10,6,3]
    Explanation:
    - The left boundary follows the path starting from the root's left child 2 -> 4.
      4 is a leaf, so the left boundary is [2].
    - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
      10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
    - The leaves from left to right are [4,7,8,9,10].
    Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -1000 <= Node.val <= 1000

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftBoundary(self,node):
        if node:
            if node.left:
                self.boundary.append(node.val)
                self.leftBoundary(node.left)
            elif node.right:
                self.boundary.append(node.val)
                self.leftBoundary(node.right)
    def rightBoundary(self,node):
        if node:
            if node.right:
                self.rightBoundary(node.right)
                self.boundary.append(node.val)
            elif node.left:
                self.rightBoundary(node.left)
                self.boundary.append(node.val)
    def leaves(self,node):
        if node:
            self.leaves(node.left)
            if node.left is None and node.right is None:
                self.boundary.append(node.val)
            self.leaves(node.right)
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        self.boundary = []
        if root:
            self.boundary.append(root.val)
            self.leftBoundary(root.left)
            self.leaves(root.left)
            self.leaves(root.right)
            self.rightBoundary(root.right)
        return self.boundary
```
