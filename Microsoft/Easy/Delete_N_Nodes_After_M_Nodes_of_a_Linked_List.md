# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Delete_N_Nodes_After_M_Nodes_of_a_Linked_List
<h1>Delete N Nodes After M Nodes of a Linked List</h1>

<p>
Given the head of a linked list and two integers m and n. Traverse the linked list and remove some nodes in the following way:
</p>

* Start with the head as the current node.
* Keep the first m nodes starting with the current node.
* Remove the next n nodes
* Keep repeating steps 2 and 3 until you reach the end of the list.
<p>
Return the head of the modified list after removing the mentioned nodes.
<br>
Follow up question: How can you solve this problem by modifying the list in-place?
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/06/06/sample_1_1848.png">

    Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
    Output: [1,2,6,7,11,12]
    Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  (1 ->2) show in black nodes.
    Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
    Continue with the same procedure until reaching the tail of the Linked List.
    Head of linked list after removing nodes is returned.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/06/06/sample_2_1848.png">

    Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
    Output: [1,5,9]
    Explanation: Head of linked list after removing nodes is returned.
    
<b>Example 3:</b>

    Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
    Output: [1,2,3,5,6,7,9,10,11]
    
<b>Constraints:</b>

- The given linked list will contain between 1 and 10^4 nodes.
- The value of each node in the linked list will be in the range [1, 10^6].
- 1 <= m,n <= 1000

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        prev = None
        while curr:
            m_c,n_c = m,n
            while curr and m_c>0:
                prev = curr
                curr = curr.next
                m_c-=1
            while curr and n_c>0:
                curr = curr.next
                n_c-=1
            prev.next = curr
        return head
```
