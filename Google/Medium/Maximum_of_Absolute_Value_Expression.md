# [Home](./../..)/[Google](./..)/[Medium](./)/Maximum_of_Absolute_Value_Expression
<h1>Maximum of Absolute Value Expression</h1>

<p>
Given two arrays of integers with equal lengths, return the maximum value of:
<br>
|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
<br>
where the maximum is taken over all 0 <= i, j < arr1.length.
</p>

<b>Example 1:</b>

    Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
    Output: 13
  
<b>Example 2:</b>

    Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
    Output: 20
 
<b>Constraints:</b>

* 2 <= arr1.length == arr2.length <= 40000
* -10^6 <= arr1[i], arr2[i] <= 10^6

<h2>Solution</h2>

```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        points = []
        for i, (x, y) in enumerate(zip(arr1, arr2)):
            points.append((
                x + y + i, 
                x + y - i,
                x - y + i,
                x - y - i
            ))
        return max(max(dim) - min(dim) for dim in zip(*points))
```
