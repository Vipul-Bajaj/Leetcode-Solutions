# [Home](./../..)/[Google](./..)/[Medium](./)/Linked_List_Components
<h1>Linked List Components</h1>

<p>
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.
</p>
<p>
Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg">

    Input: head = [0,1,2,3], nums = [0,1,3]
    Output: 2
    Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg">

    Input: head = [0,1,2,3,4], nums = [0,3,1,4]
    Output: 2
    Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

<b>Constraints:</b>

- The number of nodes in the linked list is n.
- 1 <= n <= 104
- 0 <= Node.val < n
- All the values Node.val are unique.
- 1 <= nums.length <= n
- 0 <= nums[i] <= n
- All the values of nums are unique.
<h2>Solution</h2>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        c = 0
        flag = False
        while curr:
            if curr.val in nums:
                if not flag:
                    c+=1
                    flag = True
            else:
                flag = False
            curr = curr.next
        return c
```
