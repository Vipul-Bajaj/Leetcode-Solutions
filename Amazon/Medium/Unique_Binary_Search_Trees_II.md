# [Home](./../..)/[Amazon](./..)/[Medium](./)/Unique_Binary_Search_Trees_II
<h1>Unique Binary Search Trees II</h1>

<p>
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg">

    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

<b>Example 2:</b>

    Input: n = 1
    Output: [[1]]
    
<b>Constraints:</b>

- 1 <= n <= 8

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start,end):
            if start > end:
                return [None]
            
            out = []
            for i in range(start,end+1):
                left = generate(start,i-1)
                right = generate(i+1,end)
                
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        out.append(curr)
            return out
        
        return generate(1,n) if n else []
```
