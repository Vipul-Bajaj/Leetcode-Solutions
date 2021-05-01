<h1>Leftmost Column with at Least a One</h1>

<p>
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-5.jpg">

    Input: mat = [[0,0],[1,1]]
    Output: 0
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-4.jpg">

    Input: mat = [[0,0],[0,1]]
    Output: 1
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/25/untitled-diagram-3.jpg">

    Input: mat = [[0,0],[0,0]]
    Output: -1

<b>Constraints:</b>

- rows == mat.length
- cols == mat[i].length
- 1 <= rows, cols <= 100
- mat[i][j] is either 0 or 1.
- mat[i] is sorted in non-decreasing order.

<h2>Solution</h2>

```python
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# O(m.log n) solution using binary search
# class Solution:
#     def binarySearch(self,binaryMatrix,row,n,target):
#         low,high = 0,n-1
#         start = -1
#         while low<=high:
#             mid = (low+high)//2
#             mid_ele = binaryMatrix.get(row,mid)
#             if (mid_ele == target and mid == low) or (mid_ele== target and binaryMatrix.get(row,mid-1)< target):
#                 start = mid
#             if mid_ele>=target:
#                 high = mid-1
#             else:
#                 low = mid+1
#         return start
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         row,col = binaryMatrix.dimensions()
#         min_idx = []
#         for i in range(row):
#             idx = self.binarySearch(binaryMatrix,i,col,1)
#             if idx == 0:
#                 return 0
#             if idx !=-1:
#                 min_idx.append(idx)
#         return min(min_idx) if len(min_idx)>0 else -1 
        
# O(M+N) Solution    
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row,col = binaryMatrix.dimensions()
        i,j = 0,col-1
        int_max = 2**31
        min_idx = int_max
        while i<row and j>=0:
            ele = binaryMatrix.get(i,j)
            if ele == 1:
                min_idx = min(min_idx,j)
                j-=1
            else:
                i+=1
        return min_idx if min_idx!=int_max else -1
```
