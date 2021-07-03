# [Home](./../..)/[Facebook](./..)/[Medium](./)/Find_K_Closest_Elements
<h1>Find K Closest Elements</h1>

<p>
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
</p>
<p>
An integer a is closer to x than an integer b if:
</p>

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

<b>Example 1:</b>

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

<b>Example 2:</b>

    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]
    
<b>Constraints:</b>

- 1 <= k <= arr.length
- 1 <= arr.length <= 104
- arr is sorted in ascending order.
- -104 <= arr[i], x <= 104

<h2>Solution</h2>

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
```
