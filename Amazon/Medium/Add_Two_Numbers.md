<h1>Add Two Numbers</h1>

<p>
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

</p>

<b>Example 1:</b>

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
  
<b>Example 2:</b>

    Input: l1 = [0], l2 = [0]
    Output: [0].
    
 <b>Example 3:</b>
 
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
 
<b>Constraints:</b>

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = None
        first = l1
        second = l2
        carry = 0
        while first and second:
            prev = first
            ans = first.val + second.val + carry
            carry = ans//10
            ans = ans%10
            first.val = ans
            first = first.next
            second = second.next
            
        while first:
            ans = first.val + carry
            carry = ans//10
            ans = ans%10
            first.val = ans
            first = first.next
            prev = prev.next
            
        while second:
            ans = second.val + carry
            carry = ans//10
            ans = ans%10
            prev.next = ListNode(val=ans)
            prev = prev.next
            second = second.next
        
        if carry:
            prev.next = ListNode(val=carry)
            
        return l1
```
