# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Search_a_2D_Matrix_II
<h1>Search a 2D Matrix II</h1>

<p>
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg">

    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg">

    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
    Output: false
 
<b>Constraints:</b>

- m == matrix.length
- n == matrix[i].length
- 1 <= n, m <= 300
- -109 <= matix[i][j] <= 109
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- -109 <= target <= 109

<h2>Solution</h2>

```python
# #   Binary Search Approch - Time Complexity- O(mlogn)
# class Solution:
#     def binary_search(self,arr,data):
#         low = 0
#         high = len(arr)-1
        
#         while low<=high:
#             mid = (low+high)//2
#             if arr[mid] == data:
#                 return True
#             elif arr[mid] > data:
#                 high = mid-1
#             else:
#                 low = mid+1
#         return False

#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         result = False
#         for row in matrix:
#             if row[0]<=target<=row[len(row)-1]:
#                 result = self.binary_search(row,target)
#             if result:
#                 break
        
#         return result
#   Search Space Reduction - Time Complexity- O(n+m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
```
