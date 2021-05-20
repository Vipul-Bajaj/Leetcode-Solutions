# [Home](./../..)/[Amazon](./..)/[Medium](./)/Recover_a_Tree_From_Preorder_Traversal
<h1>Recover a Tree From Preorder Traversal</h1>

<p>
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-preorder-traversal.png">

    Input: traversal = "1-2--3--4-5--6--7"
    Output: [1,2,5,3,4,6,7]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114101-pm.png">

    Input: traversal = "1-2--3---4-5--6---7"
    Output: [1,2,5,3,null,6,null,4,null,7]
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114955-pm.png">

    Input: traversal = "1-401--349---90--88"
    Output: [1,401,null,349,88,90]
    
<b>Constraints:</b>

- The number of nodes in the original tree is in the range [1, 1000].
- 1 <= Node.val <= 109

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        st = []
        dash = 0
        level = 1
        for i,x in enumerate(traversal.split("-")):
            if i==0:
                st.append([TreeNode(x),0])
                continue
            if x == '':
                dash+=1
            else:
                node = TreeNode(x)
                while st[-1][1] != level+dash-1:
                    st.pop()
                if not st[-1][0].left:
                    st[-1][0].left = node
                elif not st[-1][0].right:
                    st[-1][0].right = node
                st.append([node,level+dash])
                level = 1
                dash = 0
        return st[0][0]
```
