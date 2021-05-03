# [Home](./../..)/[Amazon](./..)/[Medium](./)/Search_a_2D_Matrix
<h1>Search a 2D Matrix</h1>

<p>
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg">

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg">

    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
 
<b>Constraints:</b>

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

<h2>Solution</h2>

```python
class Solution:
    def binary_search(self,arr,data):
        low = 0
        high = len(arr)-1
        
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == data:
                return True
            elif arr[mid] > data:
                high = mid-1
            else:
                low = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                return self.binary_search(row,target)
        return False
```
