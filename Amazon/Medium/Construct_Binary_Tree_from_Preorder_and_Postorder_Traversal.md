# [Home](./../..)/[Amazon](./..)/[Medium](./)/Construct_Binary_Tree_from_Preorder_and_Postorder_Traversal
<h1>Construct Binary Tree from Preorder and Postorder Traversal</h1>

<p>
Return any binary tree that matches the given preorder and postorder traversals.
</p>
<p>
Values in the traversals pre and post are distinct positive integers.
</p>

<b>Example 1:</b>

    Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
    Output: [1,2,3,4,5,6,7]
    
<b>Constraints:</b>

- 1 <= pre.length == post.length <= 30
- pre[] and post[] are both permutations of 1, 2, ..., pre.length.
- It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
```
