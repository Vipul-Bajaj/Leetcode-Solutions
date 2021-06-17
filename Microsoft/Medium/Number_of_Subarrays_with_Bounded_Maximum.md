# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Number_of_Subarrays_with_Bounded_Maximum
<h1>Number of Subarrays with Bounded Maximum</h1>

<p>
We are given an array nums of positive integers, and two positive integers left and right (left <= right).
</p>
<p>
Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.
</p>

<b>Example 1:</b>

    Input: 
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

<b>Constraints:</b>

- left, right, and nums[i] will be an integer in the range [0, 109].
- The length of nums will be in the range of [1, 50000].
<h2>Solution</h2>

```python
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = cur = 0
            for x in nums :
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(right) - count(left-1)
```
