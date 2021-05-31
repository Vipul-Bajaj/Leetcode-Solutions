# [Home](./../..)/[Amazon](./..)/[Medium](./)/Swapping_Nodes_in_a_Linked_List
<h1>Swapping Nodes in a Linked List</h1>

<p>
You are given the head of a linked list, and an integer k.
</p>
<p>
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg">

    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
    
<b>Example 2:</b>

    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
    
<b>Example 3:</b>

    Input: head = [1], k = 1
    Output: [1]

<b>Example 4:</b>

    Input: head = [1,2], k = 1
    Output: [2,1]

<b>Constraints:</b>

- The number of nodes in the list is n.
- 1 <= k <= n <= 105

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        c = 0
        curr = head
        first=None
        last = None
        while curr:
            if last:
                last = last.next
            elif c == k-1 and not first:
                first = curr
                last = head
            c+=1
            curr = curr.next
        first.val,last.val = last.val,first.val
        return head
```
