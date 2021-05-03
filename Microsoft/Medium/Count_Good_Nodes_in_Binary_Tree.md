# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Count_Good_Nodes_in_Binary_Tree
<h1>Count Good Nodes in Binary Tree</h1>

<p>
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png">

    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png">

    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
    
<b>Example 3:</b>

    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

<b>Constraints:</b>

- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node:
            return
        if (not self.q) or (self.q and max(self.q)<=node.val):
            self.count+=1
        self.q.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        self.q.pop()
        
    def goodNodes(self, root: TreeNode) -> int:
        self.q = []
        self.count = 0
        self.dfs(root)
        return self.count
```
