# [Home](./../..)/[Facebook](./..)/[Medium](./)/All_Elements_in_Two_Binary_Search_Trees
<h1>All Elements in Two Binary Search Trees</h1>

<p>
Given two binary search trees root1 and root2.
</p>
<p>
Return a list containing all the integers from both trees sorted in ascending order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png">

    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]
    
<b>Example 2:</b>

    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]

<b>Example 3:</b>

    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]

<b>Example 4:</b>

    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]

<b>Constraints:</b>

- Each tree has at most 5000 nodes.
- Each node's value is between [-10^5, 10^5].

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        out = []
        st1 = []
        st2 = []
        
        while st1 or st2 or root1 or root2:
            while root1:
                st1.append(root1)
                root1 = root1.left
            while root2:
                st2.append(root2)
                root2 = root2.left
            
            if not st2 or st1 and st1[-1].val<=st2[-1].val:
                root1 = st1.pop()
                out.append(root1.val)
                root1 = root1.right
            else:
                root2 = st2.pop()
                out.append(root2.val)
                root2 = root2.right
        return out
```
