# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Flipping_an_Image
<h1>Flipping an Image</h1>

<p>
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
</p>
<p>
To flip an image horizontally means that each row of the image is reversed.
</p>

* For example, flipping [1,1,0] horizontally results in [0,1,1].

<p>
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
</p>

* For example, inverting [0,1,1] results in [1,0,0].
</p>

<b>Example 1:</b>

    Input: image = [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
    
<b>Example 2:</b>

    Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

<b>Constraints:</b>

- n == image.length
- n == image[i].length
- 1 <= n <= 20
- images[i][j] is either 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = [int(not(x)) for x in image[i][::-1]]
            
        return image
```
