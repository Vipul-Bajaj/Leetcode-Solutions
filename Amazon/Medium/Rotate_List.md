# [Home](./../..)/[Amazon](./..)/[Medium](./)/Rotate_List
<h1>Rotate List</h1>

<p>
Given the head of a linked list, rotate the list to the right by k places.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg">

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg">

    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

<b>Constraints:</b>

- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k ==0 or not head:
            return head
        n = 0
        prev = None
        curr = head
        while curr:
            prev = curr
            n+=1
            curr = curr.next
        k = k%n
        if k==0:
            return head
        c = 0
        curr = head
        while c<n-k-1 and curr:
            curr = curr.next
            c+=1
        new_head = curr.next
        prev.next = head
        curr.next = None
        return new_head
```
