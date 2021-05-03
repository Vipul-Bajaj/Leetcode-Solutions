# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Remove_Linked_List_Elements
<h1>Remove Linked List Elements</h1>

<p>
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg">

    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
    
<b>Example 2:</b>

    Input: head = [], val = 1
    Output: []
    
<b>Example 3:</b>

    Input: head = [7,7,7,7], val = 7
    Output: []

<b>Constraints:</b>

- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= k <= 50

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            if curr.val == val:
                if prev:
                    prev.next = temp
                else:
                    head = temp
            else:
                prev = curr
            curr = temp
        return head
```
