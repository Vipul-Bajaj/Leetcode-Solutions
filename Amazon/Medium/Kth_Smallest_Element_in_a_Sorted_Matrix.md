# [Home](./../..)/[Amazon](./..)/[Medium](./)/Kth_Smallest_Element_in_a_Sorted_Matrix
<h1>Kth Smallest Element in a Sorted Matrix</h1>

<p>
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
</p>
<p>
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
</p>

<b>Example 1:</b>

    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

<b>Example 2:</b>

    Input: matrix = [[-5]], k = 1
    Output: -5

<b>Constraints:</b>

- n == matrix.length
- n == matrix[i].length
- 1 <= n <= 300
- -109 <= matrix[i][j] <= 109
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
- 1 <= k <= n2

<h2>Solution</h2>

```python
class Solution:
    
    def countLessEqual(self, matrix, mid, smaller, larger):
        
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
                
            else:                
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start
```
