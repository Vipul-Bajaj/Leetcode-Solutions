# [Home](./../..)/[Facebook](./..)/[Medium](./)/Construct_Binary_Tree_from_String
<h1>Construct Binary Tree from String</h1>

<p>
You need to construct a binary tree from a string consisting of parenthesis and integers.
</p>
<p>
The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
</p>
<p>
You always start to construct the left child node of the parent first if it exists.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/02/butree.jpg">

    Input: s = "4(2(3)(1))(6(5))"
    Output: [4,2,6,3,1,5]

<b>Example 2:</b>

    Input: s = "4(2(3)(1))(6(5)(7))"
    Output: [4,2,6,3,1,5,7]

<b>Example 3:</b>

    Input: s = "-4(2(3)(1))(6(5)(7))"
    Output: [-4,2,6,3,1,5,7]

<b>Constraints:</b>

- 0 <= s.length <= 3 * 104
- s consists of digits, '(', ')', and '-' only.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return
        s = s.split("(")
        root = TreeNode(int(s[0]))
        st = [root]
        i = 1
        while i<len(s):
            w = s[i]
            j = 0
            while j<len(w) and w[j]!=')':
                j+=1
            n = int(w[:j])                
            node = st[-1]    
            if node.left is None:
                node.left = TreeNode(n)
                st.append(node.left)
            else:
                node.right = TreeNode(n)
                st.append(node.right)
            while j<len(w) and w[j] == ')':
                j+=1
                st.pop()
            i+=1
        return root
```
