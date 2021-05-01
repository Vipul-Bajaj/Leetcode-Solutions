<h1>Sum Root to Leaf Numbers</h1>

<p>
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg">

    Input: root = [1,2,3]
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg">

    Input: root = [4,9,0,5,1]
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 9
- The depth of the tree will not exceed 10.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSumPath(self,node,curr_num,path_sum):
        if not node:
            return
        if node and node.left is None and node.right is None:
            path_sum[0]+=int("".join(curr_num + [str(node.val)]))
        curr_num.append(str(node.val))
        if node.left:
            self.hasSumPath(node.left,curr_num,path_sum)
        if node.right:
            self.hasSumPath(node.right,curr_num,path_sum)
        curr_num.pop()
        return 
    
    def sumNumbers(self, root: TreeNode) -> int:
        path_sum = [0]
        self.hasSumPath(root,[],path_sum)
        return path_sum[0]
```
