# [Home](./../..)/[Amazon](./..)/[Medium](./)/Reorder_List
<h1>Reorder List</h1>

<p>
You are given the head of a singly linked-list. The list can be represented as:
</p>

    L0 → L1 → … → Ln - 1 → Ln
<p>    
Reorder the list to be on the following form:
</p>

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
<p>    
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg">

    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg">

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

<b>Constraints:</b>

- The number of nodes in the list is in the range [1, 5 * 104].
- 1 <= Node.val <= 1000

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if not fast:
            prev.next = None
        mid = slow
        
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        start = head
        end = prev
        while end:
            temp1 = start.next
            temp2 = end.next
            start.next = end
            end.next = temp1
            start = temp1
            end = temp2
        
        return head
```
