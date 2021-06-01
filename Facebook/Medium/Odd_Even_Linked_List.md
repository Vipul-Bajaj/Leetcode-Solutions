# [Home](./../..)/[Facebook](./..)/[Medium](./)/Odd_Even_Linked_List
<h1>Odd Even Linked List</h1>

<p>
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
</p>
<p>
The first node is considered odd, and the second node is even, and so on.
</p>
<p>
Note that the relative order inside both the even and odd groups should remain as it was in the input.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg">

    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg">

    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
    
<b>Constraints:</b>

- The number of nodes in the linked list is in the range [0, 104].
- -106 <= Node.val <= 106
<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd_tail = ListNode(None)
        even_head = even_tail = ListNode(None)
        odd = True
        curr = head
        while curr:
            temp = curr.next
            curr.next = None
            if odd:
                odd_tail.next = curr
                odd_tail = odd_tail.next
            else:
                even_tail.next = curr
                even_tail = even_tail.next
            odd = not odd
            curr = temp
        odd_tail.next = even_head.next
        return odd_head.next
```
