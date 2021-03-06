# [Home](./../..)/[Facebook](./..)/[Medium](./)/All_Nodes_Distance_K_in_Binary_Tree
<h1>All Nodes Distance K in Binary Tree</h1>

<p>
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
</p>

<b>Example 1:</b>

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png">

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    Output: [7,4,1]

    Explanation: 
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.
    Note that the inputs "root" and "target" are actually TreeNodes.
    The descriptions of the inputs above are just serializations of these objects.

<b>Constraints:</b>

- The given tree is non-empty.
- Each node in the tree has unique values 0 <= node.val <= 500.
- The target node is a node in the tree.
- 0 <= K <= 1000.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,node,par):
        if node:
            self.parent[node] = par
            self.dfs(node.left,node)
            self.dfs(node.right,node)
            
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.parent = dict()
        
        self.dfs(root,None)
        
        q = deque([(target,0)])
        seen = set([target])
        while q:
            if q[0][1] == K:
                return [node.val for node, d in q]
            node,d = q.popleft()
            for n in (node.left,node.right,self.parent[node]):
                if n and n not in seen:
                    seen.add(n)
                    q.append((n,d+1))
        return []
```
