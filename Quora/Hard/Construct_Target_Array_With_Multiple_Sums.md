# [Home](./../..)/[Quora](./..)/[Hard](./)/Construct_Target_Array_With_Multiple_Sums
<h1>Construct Target Array With Multiple Sums</h1>

<p>
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

* let x be the sum of all elements currently in your array.
* choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
* You may repeat this procedure as many times as needed.

Return True if it is possible to construct the target array from A otherwise return False.
</p>

<b>Example 1:</b>

    Input: target = [9,3,5]
    Output: true
    Explanation: Start with [1, 1, 1] 
    [1, 1, 1], sum = 3 choose index 1
    [1, 3, 1], sum = 5 choose index 2
    [1, 3, 5], sum = 9 choose index 0
    [9, 3, 5] Done
    
<b>Example 2:</b>

    Input: target = [1,1,1,2]
    Output: false
    Explanation: Impossible to create target array from [1,1,1,1].
    
<b>Example 3:</b>

    Input: target = [8,5]
    Output: true

<b>Constraints:</b>

- N == target.length
- 1 <= target.length <= 5 * 10^4
- 1 <= target[i] <= 10^9

<h2>Solution</h2>

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        s = sum(target)
        hq = []
        for i in target:
            heapq.heappush(hq,-i)    
        while -hq[0]>1:
            max_ele = -1*heapq.heappop(hq)
            rest = s - max_ele
            if rest == 1:
                return True
            if rest<1:
                return False
            new_ele = max_ele%rest
            if new_ele==0 or new_ele == max_ele:
                return False
            heapq.heappush(hq,-new_ele)
            s = s - max_ele+new_ele

        return True
```
