<h1>Palindrome Linked List</h1>

<p>
Given the head of a singly linked list, return true if it is a palindrome.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg">

    Input: head = [1,2,2,1]
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg">

    Input: head = [1,2]
    Output: false

<b>Constraints:</b>

- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            curr = slow.next
            slow.next = None    
        else:
            curr = slow
            prev.next = None
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list1 = head
        list2 = prev
        
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True
```
