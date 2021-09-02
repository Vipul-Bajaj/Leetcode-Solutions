# [Home](./../..)/[Apple](./..)/[Medium](./)/Most_Frequent_Subtree_Sum
<h1>Most Frequent Subtree Sum</h1>

<p>
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.
</p>
<p>
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
</p>

<b>Example 1:</b>

<img src ="https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg" >

    Input: root = [5,2,-3]
    Output: [2,-3,4]

<b>Example 2:</b>

<img src ="https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg" >

    Input: root = [5,2,-5]
    Output: [2]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 105

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.freq[left+right+node.val]+=1
        return left+right+node.val
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.freq = defaultdict(int)
        self.dfs(root)
        most = max(self.freq.values())
        out = []
        for k,v in self.freq.items():
            if most == v:
                out.append(k)
        return out
```
