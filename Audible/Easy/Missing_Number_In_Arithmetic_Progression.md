<h1>Missing Number In Arithmetic Progression</h1>

<p>
In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

A value from arr was removed that was not the first or last value in the array.

Given arr, return the removed value.

<b>Example 1:</b>

    Input: arr = [5,7,11,13]
    Output: 9
    Explanation: The previous array was [5,7,9,11,13].
    
<b>Example 2:</b>

    Input: arr = [15,13,12]
    Output: 14
    Explanation: The previous array was [15,14,13,12].

<b>Constraints:</b>

- 3 <= arr.length <= 1000
- 0 <= arr[i] <= 105
- The given array is guaranteed to be a valid array.

<h2>Solution</h2>

```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1]-arr[0])//n
        next_num = arr[0]
        for num in arr:
            if num != next_num:
                return next_num
            next_num+=d
        return next_num
```
