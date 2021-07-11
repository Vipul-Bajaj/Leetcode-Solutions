# [Home](./../..)/[Facebook](./..)/[Medium](./)/Populating_Next_Right_Pointers_in_Each_Node
<h1>Populating Next Right Pointers in Each Node</h1>

<p>
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
</p>

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }

<p>
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
</p>
<p>
Initially, all next pointers are set to NULL.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png">

    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

<b>Constraints:</b>

- The number of nodes in the given tree is less than 4096.
- -1000 <= node.val <= 1000

<h2>Solution</h2>

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root,None])
        last = None
        while q:
            node = q.popleft()
            if node:
                node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if q:
                    q.append(None)
        return root
```
