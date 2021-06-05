# [Home](./../..)/[Google](./..)/[Hard](./)/Maximal_Rectangle
<h1>Maximal Rectangle</h1>

<p>
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg">

    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6
    Explanation: The maximal rectangle is shown in the above picture.
    
<b>Example 2:</b>

    Input: matrix = []
    Output: 0

<b>Constraints:</b>

- rows == matrix.length
- cols == matrix[i].length
- 0 <= row, cols <= 200
- matrix[i][j] is '0' or '1'.

<h2>Solution</h2>

```python
class Solution:
    def largestRect(self,row,n):
        st = [-1]
        max_area = 0
        for i,h in enumerate(row):
            while st[-1]!=-1 and row[st[-1]]>h:
                max_area = max(max_area,int(row[st.pop()])*(i-st[-1]-1))
            st.append(i)
        while st[-1]!=-1:
            max_area = max(max_area,int(row[st.pop()])*(n-st[-1]-1))
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m<=0:
            return 0
        n = len(matrix[0])
        
        res = 0
        dp = [0]*n
        
        for i in range(0,m):
            for j in range(n):
                dp[j] = dp[j]+1 if matrix[i][j]=='1' else 0
            res = max(res,self.largestRect(dp,n))
        
        return res
```
