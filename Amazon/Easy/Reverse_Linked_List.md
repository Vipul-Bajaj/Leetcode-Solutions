# [Home](./../../..)/[Amazon](./../..)/[Easy](./..)/Reverse_Linked_List
# [Home](./../../..)/[Amazon](./../..)/[Easy](./..)/Reverse_Linked_List
<h1>Reverse Linked List</h1>

<p>
Given the head of a singly linked list, reverse the list, and return the reversed list.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg">

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg">

    Input: head = [1,2]
    Output: [2,1]
    
<b>Example 3:</b>

    Input: head = []
    Output: []

<b>Constraints:</b>

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
```
