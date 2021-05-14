# [Home](./../..)/[Amazon](./..)/[Medium](./)/Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List
<h1>Remove Zero Sum Consecutive Nodes from Linked List</h1>

<p>
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)
</p>

<b>Example 1:</b>

    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.
    
<b>Example 2:</b>

    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]
    
<b>Example 3:</b>

    Input: head = [1,2,3,-3,-2]
    Output: [1]

<b>Constraints:</b>

- The given linked list will contain between 1 and 1000 nodes.
- Each node in the linked list has -1000 <= node.val <= 1000.

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        d = {0:dummy} # key is the prefix sum, value is the last node of getting this sum value, which is l5
        while head:
            prefix += head.val
            d[prefix] = head
            head = head.next
		# Go from the dummy node again to set the next node to be the last node for a prefix sum 
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next
        
        return dummy.next
```
