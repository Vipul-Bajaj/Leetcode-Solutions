<h1>Remove Nth Node From End of List</h1>

<p>
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg">

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    
<b>Example 2:</b>

    Input: head = [1], n = 1
    Output: []
    
<b>Example 3:</b>

    Input: head = [1,2], n = 1
    Output: [1]

<b>Constraints:</b>

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        curr = head
        prev = None
        c = 0
        while curr and c<length-n:
            prev = curr
            curr = curr.next
            c+=1
        if prev:
            prev.next = curr.next if curr else None
        else:
            head = head.next
        
        return head
```
