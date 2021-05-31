# [Home](./../..)/[JPMorgan](./..)/[Easy](./)/Convert_Binary_Number_in_a_Linked_List_to_Integer
<h1>Convert Binary Number in a Linked List to Integer</h1>

<p>
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
</p>
<p>
Return the decimal value of the number in the linked list.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/12/05/graph-1.png">

    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    
<b>Example 2:</b>

    Input: head = [0]
    Output: 0
    
<b>Example 3:</b>

    Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    Output: 18880

<b>Constraints:</b>

- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num<<1)|head.next.val
            head = head.next
        return num
```
