# [Home](./../..)/[Amazon](./..)/[Medium](./)/Linked_List_Cycle_II
<h1>Linked List Cycle II</h1>

<p>
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png">

    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png">

    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png">

    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

<b>Constraints:</b>

- The number of the nodes in the list is in the range [0, 104].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        if has_cycle:
            fast = head
            while fast!= slow:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
```
