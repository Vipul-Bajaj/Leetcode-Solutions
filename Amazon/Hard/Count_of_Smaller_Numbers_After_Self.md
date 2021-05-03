# [Home](./../../..)/[Amazon](./../..)/[Hard](./..)/Count_of_Smaller_Numbers_After_Self
<h1>Count of Smaller Numbers After Self</h1>

<p>
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

</p>

<b>Example 1:</b>

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    
<b>Example 2:</b>

    Input: nums = [-1]
    Output: [0]
    
<b>Example 3:</b>

    Input: nums = [-1,-1]
    Output: [0,0]

<b>Constraints:</b>

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104

<h2>Solution</h2>

```python
# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.ele_count = 1
#         self.left_count = 0
# class Tree:
#     def __init__(self,node):
#         self.root = node
#     def insert(self,node):
#         cnt = 0
#         curr = self.root
#         prev = None
#         while curr:
#             prev = curr
#             if node.val>curr.val:
#                 cnt+= (curr.ele_count + curr.left_count)
#                 curr = curr.right
#             elif node.val<curr.val:
#                 curr.left_count+=1
#                 curr = curr.left
#             else:
#                 prev.ele_count+=1
#                 break
#         if node.val>prev.val:
#             prev.right = node
#         elif node.val<prev.val:
#             prev.left = node
#         else:
#             return cnt+prev.left_count
#         return cnt
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         count = [0]

#         tree = Tree(TreeNode(nums[-1]))
#         for i in range(n-2,-1,-1):
#             count.append(tree.insert(TreeNode(nums[i])))
#         return count[::-1]
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result, arr = [0] * len(nums), []
        for i in range(len(nums) - 1, -1, -1):
            index = bisect_left(arr, nums[i])
            result[i] = index
            arr.insert(index, nums[i])
        return result
```
