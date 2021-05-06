# [Home](./../..)/[Facebook](./..)/[Medium](./)/Convert_Sorted_List_to_Binary_Search_Tree
<h1>Convert Sorted List to Binary Search Tree</h1>

<p>
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg">

    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
    
<b>Example 2:</b>

    Input: head = []
    Output: []
    
<b>Example 3:</b>

    Input: head = [0]
    Output: [0]

<b>Constraints:</b>

- The number of nodes in head is in the range [0, 2 * 104].
- -10^5 <= Node.val <= 10^5

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createTree(self,n):
        if n<=0:
            return
        left = self.createTree(n//2)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.createTree( n - (n//2) - 1) 
        return root 
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n+=1
        return self.createTree(n)
```
