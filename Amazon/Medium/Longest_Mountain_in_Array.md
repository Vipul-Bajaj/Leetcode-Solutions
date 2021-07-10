# [Home](./../..)/[Amazon](./..)/[Medium](./)/Longest_Mountain_in_Array
<h1>Longest Mountain in Array</h1>

<p>
You may recall that an array arr is a mountain array if and only if:
</p>

* arr.length >= 3
* There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

<p>
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
</p>

<b>Example 1:</b>

    Input: arr = [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
    
<b>Example 2:</b>

    Input: arr = [2,2,2]
    Output: 0
    Explanation: There is no mountain.

<b>Constraints:</b>

- 1 <= arr.length <= 104
- 0 <= arr[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left = ans = 0
        while left<n:
            right = left
            if right+1<n and arr[right]<arr[right+1]:
                while right+1<n and arr[right]<arr[right+1]:
                    right+=1
                
                if right+1<n and arr[right]>arr[right+1]:
                    while right+1<n and arr[right]>arr[right+1]:
                        right+=1
                    
                    ans = max(ans,right-left+1)
            left = max(right,left+1)
        return ans
```
