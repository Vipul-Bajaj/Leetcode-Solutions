# [Home](./../..)/[Facebook](./..)/[Easy](./)/Kth_Missing_Positive_Number
<h1>Kth Missing Positive Number</h1>

<p>
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
<br>
Find the kth positive integer that is missing from this array.
</p>

<b>Example 1:</b>

    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
    
<b>Example 2:</b>

    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

<b>Constraints:</b>

- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
- 1 <= k <= 1000
- arr[i] < arr[j] for 1 <= i < j <= arr.length

<h2>Solution</h2>

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = 0
        missing = []
        for i in range(1,arr[len(arr)-1]+k+1):
            if idx<len(arr) and arr[idx] == i:
                idx+=1
            else:
                missing.append(i)
        return missing[k-1]
```
