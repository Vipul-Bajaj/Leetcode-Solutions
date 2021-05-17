# [Home](./../..)/[Adobe](./..)/[Easy](./)/Remove_Duplicates_from_Sorted_List
<h1>Remove Duplicates from Sorted List</h1>

<p>
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg">

    Input: head = [1,1,2]
    Output: [1,2]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg">

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
    
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
        prev = None
        while curr:
            if prev and curr.val == prev.val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
        return head
```
