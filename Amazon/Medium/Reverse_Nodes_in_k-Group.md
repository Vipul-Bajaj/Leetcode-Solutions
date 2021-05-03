# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Reverse_Nodes_in_k-Group
<h1>Reverse Nodes in k-Group</h1>

<p>
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

- Could you solve the problem in O(1) extra memory space?
- You may not alter the values in the list's nodes, only nodes itself may be changed.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg">

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg">

    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    
<b>Example 3:</b>

    Input: head = [1,2,3,4,5], k = 1
    Output: [1,2,3,4,5]

<b>Constraints:</b>

- The number of nodes in the list is in the range sz.
- 1 <= sz <= 5000
- 0 <= Node.val <= 1000
- 1 <= k <= sz

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        
        dummy = nhead = ListNode() # the new list to insert to
        for _ in range(n//k):
            ntail = head  # the save the position for later jumping to
            for _ in range(k):
                head.next, nhead.next, head = nhead.next, head, head.next  # insert at nhead
            nhead = ntail  # move insertion point to the right by k steps
        ntail.next = head
        
        return dummy.next
```
