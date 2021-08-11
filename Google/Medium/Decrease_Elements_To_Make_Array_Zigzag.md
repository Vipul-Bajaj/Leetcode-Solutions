# [Home](./../..)/[Google](./..)/[Medium](./)/Decrease_Elements_To_Make_Array_Zigzag
<h1>Decrease Elements To Make Array Zigzag</h1>

<p>
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.
</p>
<p>
An array A is a zigzag array if either:
</p>

- Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
- OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...

<p>
Return the minimum number of moves to transform the given array nums into a zigzag array.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3]
    Output: 2
    Explanation: We can decrease 2 to 0 or 3 to 1.

<b>Example 2:</b>

    Input: nums = [9,6,1,6,2]
    Output: 4
    
<b>Constraints:</b>

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float('inf')] + nums + [float('inf')]
        res = [0, 0]
        for i in range(1, len(nums) - 1):
            res[i % 2] += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(res)
```
