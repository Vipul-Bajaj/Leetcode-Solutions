# [Home](./../..)/[Google](./..)/[Easy](./)/Peak_Index_in_a_Mountain_Array
<h1>Peak Index in a Mountain Array</h1>

<p>
Let's call an array arr a mountain if the following properties hold:
</p>

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... arr[i-1] < arr[i]
  - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

<p>
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
</p>

<b>Example 1:</b>

    Input: arr = [0,1,0]
    Output: 1
    
<b>Example 2:</b>    

    Input: arr = [0,2,1,0]
    Output: 1
    
<b>Example 3:</b>     

    Input: arr = [24,69,100,99,79,78,67,36,26,19]
    Output: 2

<b>Constraints:</b>

- 3 <= arr.length <= 104
- 0 <= arr[i] <= 106
- arr is guaranteed to be a mountain array.

<h2>Solution</h2>

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
```
