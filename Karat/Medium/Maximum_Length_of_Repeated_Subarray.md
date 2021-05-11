# [Home](./../..)/[Karat](./..)/[Medium](./)/Maximum_Length_of_Repeated_Subarray
<h1>Maximum Length of Repeated Subarray</h1>

<p>
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
</p>

<b>Example 1:</b>

    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
    
<b>Example 2:</b>

    Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    Output: 5

<b>Constraints:</b>

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100

<h2>Solution</h2>

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1),len(nums2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    continue
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
        max_len = 0
        for row in dp:
            max_len = max(max_len,max(row))
        return max_len
```
