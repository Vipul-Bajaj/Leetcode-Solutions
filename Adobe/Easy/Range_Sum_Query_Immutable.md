# [Home](./../..)/[Adobe](./..)/[Easy](./)/Range_Sum_Query_Immutable
<h1>Range Sum Query - Immutable</h1>

<p>
Given an integer array nums, handle multiple queries of the following type:
</p>

- Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

<p>
Implement the NumArray class:
</p>

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

<b>Example 1:</b>

    Input
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
    [null, 1, -1, -3]

    Explanation
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -105 <= nums[i] <= 105
- 0 <= left <= right < nums.length
- At most 104 calls will be made to sumRange.

<h2>Solution</h2>

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```
