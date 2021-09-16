# [Home](./../..)/[Amazon](./..)/[Medium](./)/Longest_Turbulent_Subarray
<h1>Longest Turbulent Subarray</h1>

<p>
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
</p>
<p>
A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
</p>
<p>
More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
</p>

- For i <= k < j:
  - arr[k] > arr[k + 1] when k is odd, and
  - arr[k] < arr[k + 1] when k is even.
- Or, for i <= k < j:
  - arr[k] > arr[k + 1] when k is even, and
  - arr[k] < arr[k + 1] when k is odd.
</p>

<b>Example 1:</b>

    Input: arr = [9,4,2,10,7,8,8,1,9]
    Output: 5
    Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

<b>Example 2:</b>

    Input: arr = [4,8,12,16]
    Output: 2

<b>Example 3:</b>

    Input: arr = [100]
    Output: 1

<b>Constraints:</b>

- 1 <= arr.length <= 4 * 104
- 0 <= arr[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def cmp(a,b):
            if a == b:
                return 0
            if a>b:
                return 1
            return -1
        n = len(arr)
        ans = 1
        anchor = 0
        for i in range(1,n):
            c = cmp(arr[i-1],arr[i])
            if c== 0:
                anchor = i
            elif i == n-1 or c*cmp(arr[i],arr[i+1])!=-1:
                ans = max(ans,i-anchor+1)
                anchor = i
        return ans
```
