# [Home](./../..)/[Amazon](./..)/[Medium](./)/Pseudo_Palindromic_Paths_in_a_Binary_Tree
<h1>Pseudo-Palindromic Paths in a Binary Tree</h1>

<p>
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png">

    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/05/07/palindromic_paths_2.png">

    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
    
<b>Example 3:</b>

    Input: root = [9]
    Output: 1

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 105].
- 1 <= Node.val <= 9

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPaths(self, node,counter,path_len,count):
        if not node:
            return
        if node and not node.left and not node.right:
            counter[node.val]+=1
            pal_len = path_len[0] + 1
            for i in counter.values():
                if i%2==0:
                    pal_len-=i
                    continue
                pal_len-=i-1
            if pal_len == 0 or pal_len-1==0:
                count[0]+=1
            counter[node.val]-=1
            return
        counter[node.val]+=1
        path_len[0]+=1
        if node.left:
            self.getPaths(node.left,counter,path_len,count)
        if node.right:
            self.getPaths(node.right,counter,path_len,count)
        counter[node.val]-=1
        path_len[0]-=1
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:  
        counter = defaultdict(int)
        count = [0]
        self.getPaths(root,counter,[0],count)
        return count[0]
```
