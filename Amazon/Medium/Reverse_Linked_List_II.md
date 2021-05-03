# [Home](./../..)/[Amazon](./..)/[Medium](./)/Reverse_Linked_List_II
<h1> Reverse Linked List II</h1>

<p>
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg">

    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    
<b>Example 2:</b>

    Input: head = [5], left = 1, right = 1
    Output: [5]

<b>Constraints:</b>

- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        c = 0
        curr = head
        prev = None
        while curr and c<left-1:
            prev = curr
            curr = curr.next
            c+=1
        first = prev
        last = curr
        while curr and c<right:
            temp =curr.next
            curr.next = prev
            prev = curr
            curr = temp
            c+=1
        if first:
            first.next = prev
        else:
            head = prev
        last.next = curr
        return head
```
