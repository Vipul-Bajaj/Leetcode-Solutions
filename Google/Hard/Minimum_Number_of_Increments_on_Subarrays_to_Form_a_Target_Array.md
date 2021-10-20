# [Home](./../..)/[Google](./..)/[Hard](./)/Minimum_Number_of_Increments_on_Subarrays_to_Form_a_Target_Array
<h1>Minimum Number of Increments on Subarrays to Form a Target Array</h1>

<p>
Given an array of positive integers target and an array initial of same size with all zeros.
</p>
<p>
Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:
</p>

- Choose any subarray from initial and increment each value by one.
  
<p>  
The answer is guaranteed to fit within the range of a 32-bit signed integer.
</p>

<b>Example 1:</b>

    Input: target = [1,2,3,2,1]
    Output: 3
    Explanation: We need at least 3 operations to form the target array from the initial array.
    [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
    [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
    [1,2,2,2,1] increment 1 at index 2.
    [1,2,3,2,1] target array is formed.

<b>Example 2:</b>

    Input: target = [3,1,1,2]
    Output: 4
    Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).

<b>Example 3:</b>

    Input: target = [3,1,5,4,2]
    Output: 7
    Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                      -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).

<b>Example 4:</b>

    Input: target = [1,1,1,1]
    Output: 1

<b>Constraints:</b>

- 1 <= target.length <= 10^5
- 1 <= target[i] <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        
        for t in target:
            res+=max(t-pre,0)
            pre = t
        
        return res
```
