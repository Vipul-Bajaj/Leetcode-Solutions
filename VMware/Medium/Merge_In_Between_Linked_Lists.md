# [Home](./../..)/[VMware](./..)/[Medium](./)/Merge_In_Between_Linked_Lists
<h1>Merge In Between Linked Lists</h1>

<p>
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure incidate the result:

<img src="https://assets.leetcode.com/uploads/2020/11/05/fig1.png">

Build the result list and return its head.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex1.png">

    Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    Output: [0,1,2,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png">

    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    Explanation: The blue edges and nodes in the above figure indicate the result.
    
<b>Constraints:</b>

- 3 <= list1.length <= 104
- 1 <= a <= b < list1.length - 1
- 1 <= list2.length <= 104

<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        prev_a = None
        next_b = None
        n=0
        while curr:
            if n+1 == a:
                prev_a = curr
            if n-1 == b:
                next_b = curr
                break
            n+=1
            curr = curr.next
        
        prev_a.next = list2
            
        while prev_a.next:
            prev_a = prev_a.next
        prev_a.next = next_b
        
        return list1
```
