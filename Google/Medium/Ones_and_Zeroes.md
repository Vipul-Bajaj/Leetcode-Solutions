# [Home](./../..)/[Google](./..)/[Medium](./)/Ones_and_Zeroes
<h1>Ones and Zeroes</h1>

<p>
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

</p>

<b>Example 1:</b>

    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
    Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
    {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
  
<b>Example 2:</b>

    Input: strs = ["10","0","1"], m = 1, n = 1
    Output: 2
    Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
<b>Constraints:</b>

    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100


<h2>Solution</h2>

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for j in range(n+1)]for i in range(m+1)]
        for s in strs:
            count = self.count_zeros_ones(s)
            
            for zeroes in range(m, count[0]-1,-1):
                for ones in range(n, count[1]-1,-1):
                    dp[zeroes][ones] = max(1+dp[zeroes-count[0]][ones-count[1]],dp[zeroes][ones])
                    
        return dp[m][n]
    def count_zeros_ones(self,s):
        count = [0,0]
        for i in s:
            if i == '0':
                count[0] +=1
            else:
                count[1] +=1
        return count
```
