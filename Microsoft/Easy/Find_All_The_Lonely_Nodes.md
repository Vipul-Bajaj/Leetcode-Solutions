# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Find_All_The_Lonely_Nodes
<h1>Find All The Lonely Nodes</h1>

<p>
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.
</p>
<p>
Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/06/03/e1.png">

    Input: root = [1,2,3,null,4]
    Output: [4]
    Explanation: Light blue node is the only lonely node.
    Node 1 is the root and is not lonely.
    Nodes 2 and 3 have the same parent and are not lonely.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/06/03/e2.png">

    Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
    Output: [6,2]
    Explanation: Light blue nodes are lonely nodes.
    Please remember that order doesn't matter, [2,6] is also an acceptable answer.
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2020/06/03/e3.png">

    Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
    Output: [77,55,33,66,44,22]
    Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
    All other nodes are lonely.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 1000].
- Each node's value is between [1, 10^6].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        st = [root]
        out = []
        while st:
            node = st.pop()
            if not node.left and not node.right:
                continue
            elif not node.left and node.right:
                out.append(node.right.val)
                st.append(node.right)
            elif not node.right and node.left:
                out.append(node.left.val)
                st.append(node.left)
            else:
                st.append(node.left)
                st.append(node.right)
        return out
```
