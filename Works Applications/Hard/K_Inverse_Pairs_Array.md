# [Home](./../..)/[Works Applications](./..)/[Hard](./)/K_Inverse_Pairs_Array
<h1>K Inverse Pairs Array</h1>

<p>
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
</p>
<p>
Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
</p>

<b>Example 1:</b>

    Input: n = 3, k = 0
    Output: 1
    Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
    
<b>Example 2:</b>

    Input: n = 3, k = 1
    Output: 2
    Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

<b>Constraints:</b>

- 1 <= n <= 1000
- 0 <= k <= 1000

<h2>Solution</h2>

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for j in range(k+1)]for i in range(n+1)]
        
        M = 1000000007
        
        for i in range(1,n+1):
            for j in range(k+1):
                if i == 1 and j == 0:
                    dp[i][j] = 1
                    break
                elif j == 0:
                    dp[i][j]=1
                else:
                    val = (dp[i-1][j] + M - (dp[i-1][j-i] if j-i>=0 else 0))%M
                    dp[i][j] = (dp[i][j-1]+val)%M
                    
        return dp[n][k]
```
