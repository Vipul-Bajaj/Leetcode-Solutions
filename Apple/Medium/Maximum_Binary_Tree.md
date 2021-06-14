# [Home](./../..)/[Apple](./..)/[Medium](./)/Maximum_Binary_Tree
<h1>Maximum Binary Tree</h1>

<p>
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
</p>

1. Create a root node whose value is the maximum value in nums.
2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.
 
<p>
Return the maximum binary tree built from nums.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg">

    Input: nums = [3,2,1,6,0,5]
    Output: [6,3,5,null,2,0,null,null,1]
    Explanation: The recursive calls are as follow:
    - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
        - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
            - Empty array, so no child.
            - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
                - Empty array, so no child.
                - Only one element, so child is a node with value 1.
        - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
            - Only one element, so child is a node with value 0.
            - Empty array, so no child.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg">

    Input: nums = [3,2,1]
    Output: [3,null,2,null,1]

<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
- All integers in nums are unique.

<h2>Solution</h2>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructTree(self,arr):
        if not arr:
            return None
        max_ele = max(arr)
        idx = arr.index(max_ele)
        node = TreeNode(max_ele)
        node.left = self.constructTree(arr[:idx])
        node.right = self.constructTree(arr[idx+1:])
        return node
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.constructTree(nums)
```
