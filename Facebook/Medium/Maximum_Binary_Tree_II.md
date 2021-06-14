# [Home](./../..)/[Facebook](./..)/[Medium](./)/Maximum_Binary_Tree_II
<h1>Maximum Binary Tree II</h1>

<p>
We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.
</p>
<p>
Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:
</p>
<p>
  
- If A is empty, return null.
- Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
- The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
- The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
- Return root.
  
<p>  
Note that we were not given A directly, only a root node root = Construct(A).
</p>
<p>
Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.
</p>
<p>
Return Construct(B).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-1.png">
<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png">

    Input: root = [4,1,3,null,null,2], val = 5
    Output: [5,4,null,1,3,null,null,2]
    Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-1.png">
<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-2.png">

    Input: root = [5,2,4,null,1], val = 3
    Output: [5,2,4,null,1,null,3]
    Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-1.png">
<img src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-2.png">

    Input: root = [5,2,3,null,1], val = 4
    Output: [5,2,4,null,1,3]
    Explanation: A = [2,1,5,3], B = [2,1,5,3,4]

<b>Constraints:</b>

- 1 <= B.length <= 100

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getArray(self,node,index,arr):
        if not node:
            return
        self.getArray(node.left,index,arr)
        arr.insert(len(arr)+1,node.val)
        self.getArray(node.right,len(arr)+1,arr)
    
    def constructTree(self,arr):
        if not arr:
            return None
        max_ele = max(arr)
        idx = arr.index(max_ele)
        node = TreeNode(max_ele)
        node.left = self.constructTree(arr[:idx])
        node.right = self.constructTree(arr[idx+1:])
        return node
            
    
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        arr = []
        self.getArray(root,0,arr)
        arr.append(val)
        return self.constructTree(arr)
```
