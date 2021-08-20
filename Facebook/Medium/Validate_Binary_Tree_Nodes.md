# [Home](./../..)/[Facebook](./..)/[Medium](./)/Validate_Binary_Tree_Nodes
<h1>Validate Binary Tree Nodes</h1>

<p>
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
</p>
<p>
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
</p>
<p>
Note that the nodes have no values and that we only use the node numbers in this problem.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png">

    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
    Output: true

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex2.png">

    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
    Output: false

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex3.png">

    Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
    Output: false

<b>Example 4:</b>

<img src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex4.png">

    Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
    Output: false
    
<b>Constraints:</b>

- 1 <= n <= 104
- leftChild.length == rightChild.length == n
- -1 <= leftChild[i], rightChild[i] <= n - 1

<h2>Solution</h2>

```python
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ledges = len([l for l in leftChild if l !=-1])
        redges = len([r for r in rightChild if r !=-1])
        
        if ledges+redges != n-1:
            return False
        parent = [[] for _ in range(n)]
        
        for i in range(n):
            if leftChild[i] != -1: parent[leftChild[i]].append(i)                
            if rightChild[i] != -1: parent[rightChild[i]].append(i)    
                
        roots = [i for i in range(len(parent)) if not parent[i]]

        if len(roots) != 1:
            return False
        
        root = roots[0]
        def count_nodes(root):
            if root == -1:
                return 0
            return 1 + count_nodes(leftChild[root]) + count_nodes(rightChild[root])
        
        return count_nodes(root)==n
```
