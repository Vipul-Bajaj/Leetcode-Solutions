# [Home](./../..)/[Amazon](./..)/[Easy](./)/Rank_Transform_of_an_Array
<h1>Rank Transform of an Array</h1>

<p>
Given an array of integers arr, replace each element with its rank.
</p>
<p>
The rank represents how large the element is. The rank has the following rules:
</p>

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

<b>Example 1:</b>

    Input: arr = [40,10,20,30]
    Output: [4,1,2,3]
    Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

<b>Example 2:</b>

    Input: arr = [100,100,100]
    Output: [1,1,1]
    Explanation: Same elements share the same rank.

<b>Example 3:</b>

    Input: arr = [37,12,28,9,100,56,80,5,12]
    Output: [5,3,4,2,8,6,7,1,3]


<b>Constraints:</b>

- 0 <= arr.length <= 105
- -109 <= arr[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, arr)
```
