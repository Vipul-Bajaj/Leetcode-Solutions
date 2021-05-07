# [Home](./../..)/[Amazon](./..)/[Easy](./)/Flood_Fill
<h1>Flood Fill</h1>

<p>
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
</p>

<b>Example 1:</b>

    Input: 
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: 
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.
    
<b>Constraints:</b>

- The length of image and image[0] will be in the range [1, 50].
- The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
- The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

<h2>Solution</h2>

```python
class Solution:
    def get_val(self,grid,i,j,r,c):
        if i>=r or i<0 or j>=c or j<0:
            return -1
        return grid[i][j]
    
    def dfs(self,grid,i,j,r,c,visited):
        if i>=r or i<0 or j>=c or j<0:
            return
        visited[i][j] = True
        grid[i][j] = self.newColor
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        
        for k in range(4):
            new_i = i + dirs[k][0]
            new_j = j + dirs[k][1]
            val = self.get_val(grid,new_i,new_j,r,c)
            if val == self.color and not visited[new_i][new_j]:
                self.dfs(grid,new_i,new_j,r,c,visited)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r,c = len(image),len(image[0])
        visited = [[False for j in range(c)]for i in range(r)]
        self.color = image[sr][sc]
        self.newColor = newColor
        
        self.dfs(image, sr,sc,r,c,visited)
        
        return image
```
