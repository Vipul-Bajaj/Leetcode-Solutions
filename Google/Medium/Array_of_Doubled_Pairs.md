# [Home](./../..)/[Google](./..)/[Medium](./)/Array_of_Doubled_Pairs
<h1>Array of Doubled Pairs</h1>

<p>
Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.
</p>

<b>Example 1:</b>

    Input: arr = [3,1,3,6]
    Output: false

<b>Example 2:</b>

    Input: arr = [2,1,2,6]
    Output: false

<b>Example 3:</b>

    Input: arr = [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

<b>Example 4:</b>

    Input: arr = [1,2,4,16,8,4]
    Output: false
    
<b>Constraints:</b>

- 0 <= arr.length <= 3 * 104
- arr.length is even.
- -105 <= arr[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for x in sorted(arr,key = abs):
            if count[x] == 0:continue
            if count[2*x]==0: return False
            count[x]-=1
            count[2*x]-=1
        return True
```
