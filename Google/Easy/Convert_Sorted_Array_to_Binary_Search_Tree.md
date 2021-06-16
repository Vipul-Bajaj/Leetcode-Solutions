# [Home](./../..)/[Google](./..)/[Easy](./)/Convert_Sorted_Array_to_Binary_Search_Tree
<h1>Convert Sorted Array to Binary Search Tree</h1>

<p>
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
</p>
<p>
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
</p>

<b>Example 1:</b>

    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:
    
<b>Example 2:</b>

    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

<b>Constraint:</b>

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in a strictly increasing order.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        low,high = 0,len(nums)-1
        if low>high:
            return None
        mid = (low+high)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
```
