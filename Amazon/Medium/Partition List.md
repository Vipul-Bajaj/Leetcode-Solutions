<h1>Partition List</h1>

<p>
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg"

    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    
<b>Example 2:</b>

    Input: head = [2,1], x = 2
    Output: [1,2]

<b>Constraints:</b>

- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        new_head_1,new_tail_1 = None,None
        new_head_2,new_tail_2 = None,None
        
        current = head

        while current:
            if current.val<x:
                if new_head_1 is None:
                    new_head_1 = new_tail_1 = ListNode(current.val)
                else:
                    new_tail_1.next = ListNode(current.val)
                    new_tail_1 = new_tail_1.next
            else:
                if new_head_2 is None:
                    new_head_2 = new_tail_2 = ListNode(current.val)
                else:
                    new_tail_2.next = ListNode(current.val)
                    new_tail_2 = new_tail_2.next
            current = current.next    
            
        if new_head_1:
            head = new_head_1
            new_tail_1.next = new_head_2
        else:
            head = new_head_2
            new_tail_2.next = new_head_1
        
        return head
```
