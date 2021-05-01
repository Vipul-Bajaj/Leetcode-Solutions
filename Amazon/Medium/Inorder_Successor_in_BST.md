<h1>Inorder Successor in BST</h1>

<p>
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG">

    Input: root = [2,1,3], p = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG">

    Input: root = [5,3,6,2,4,null,null,1], p = 6
    Output: null
    Explanation: There is no in-order successor of the current node, so the answer is null.
 
<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 105
- All Nodes will have unique values.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        
        while root:
            if p.val>=root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor
```
