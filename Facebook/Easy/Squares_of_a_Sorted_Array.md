# [Home](./../..)/[Facebook](./..)/[Easy](./)/Squares_of_a_Sorted_Array
<h1>Squares of a Sorted Array</h1>

<p>
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
</p>

<b>Example 1:</b>

    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    
<b>Example 2:</b>

    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

<h2>Solution</h2>

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
```
