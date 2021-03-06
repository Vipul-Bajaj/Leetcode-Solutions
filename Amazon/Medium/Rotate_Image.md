# [Home](./../..)/[Amazon](./..)/[Medium](./)/Rotate_Image
<h1>Rotate Image</h1>

<p>
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

</p>

<b>Example 1:</b>
    
<img src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg"/>
    
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
  
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg"/>

    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
<b>
 
<b>Constraints:</b>

    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000


<h2>Solution</h2>

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m,n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
```
