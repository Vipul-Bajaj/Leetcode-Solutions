# [Home](./../..)/[Amazon](./..)/[Medium](./)/Remove_Duplicates_from_Sorted_List_II
<h1>Remove Duplicates from Sorted List II</h1>

<p>
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg">

    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg">

    Input: head = [1,1,1,2,3]
    Output: [2,3]

<b>Constraints:</b>

- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        head = prev = ListNode(None)
        isDupl = False
        while curr:
            if curr.next and curr.val == curr.next.val:
                isDupl = True
            elif isDupl:
                isDupl = False
            else:
                prev.next = curr
                prev = curr
            curr = curr.next
        
        prev.next = curr
        
        return head.next
```
