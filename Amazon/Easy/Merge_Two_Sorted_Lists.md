# [Home](./../..)/[Amazon](./..)/[Easy](./)/Merge_Two_Sorted_Lists
<h1>Merge Two Sorted Lists</h1>

<p>
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg">

    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
<b>Example 2:</b>

    Input: l1 = [], l2 = []
    Output: []
    
<b>Example 3:</b>

    Input: l1 = [], l2 = [0]
    Output: [0]
 
<b>Constraints:</b>

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both l1 and l2 are sorted in non-decreasing order.

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        
        prev = head
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 else l2
        return head.next
```
