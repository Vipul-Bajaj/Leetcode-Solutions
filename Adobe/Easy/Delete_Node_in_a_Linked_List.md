<h1>Delete Node in a Linked List</h1>

<p>
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg">

    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg">

    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

<b>Example 3:</b>

    Input: head = [1,2,3,4], node = 3
    Output: [1,2,4]
    
<b>Constraints:</b>

- The number of the nodes in the given list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node
</p>

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
