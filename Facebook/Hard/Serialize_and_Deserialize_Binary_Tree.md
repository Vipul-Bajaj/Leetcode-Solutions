# [Home](./../..)/[Facebook](./..)/[Hard](./)/Serialize_and_Deserialize_Binary_Tree
<h1>Serialize and Deserialize Binary Tree</h1>

<p>
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
</p>
<p>
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
</p>
<p>
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg">

    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]
    
<b>Example 2:</b>

    Input: root = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 104].
- -1000 <= Node.val <= 1000

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def _prune(self,data):
        j = len(data)-1
        while j>=0 and data[j]=='-':
            j-=1
        return data[:j+1]

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        q = deque([root])
        while q:
            node = q.popleft()
            s.append(str(node.val) if node else "-")
            if node:
                q.append(node.left)
                q.append(node.right)    
        s = self._prune(s)
        # print(s)
        return ",".join(s)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        s = data.split(',')
        root = TreeNode(int(s[0]))
        q = deque([root])
        j = 1
        n = len(s)
        while q:
            node = q.popleft()
            if j<n and s[j] !='-':
                node.left = TreeNode(int(s[j]))
                q.append(node.left)
            j+=1
            if j<n and s[j] !='-':
                node.right = TreeNode(int(s[j]))
                q.append(node.right)
            j+=1    
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```
