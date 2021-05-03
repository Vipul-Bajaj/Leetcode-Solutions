# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Intersection_of_Two_Linked_Lists
<h1>Intersection of Two Linked Lists</h1>

<p>
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

<img src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png">

It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png">

    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'
    Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png">

    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'
    Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png">

    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection
    Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    Explanation: The two lists do not intersect, so return null.
    
<b>Constraints:</b>

- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 0 <= m, n <= 3 * 104
- 1 <= Node.val <= 105
- 0 <= skipA <= m
- 0 <= skipB <= n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.

<h2>Solution</h2>

```python
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# Using length appoach
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         n1 = 0
#         n2 = 0
#         curr1 = headA
#         curr2 = headB
        
#         while curr1:
#             curr1 = curr1.next
#             n1+=1
            
#         while curr2:
#             curr2 = curr2.next
#             n2+=1
#         c = 0
#         curr1 = headA
#         curr2 = headB
#         if n1<n2:
#             while c<n2-n1:
#                 curr2 = curr2.next
#                 c+=1
#         else:
#             while c<n1-n2:
#                 curr1 = curr1.next
#                 c+=1
        
#         while curr1 and curr2:
#             if curr1 == curr2:
#                 return curr1
#             curr1 = curr1.next
#             curr2 = curr2.next
#         return None
# Using 2 pointers approach
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
```
