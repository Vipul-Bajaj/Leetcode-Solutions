# [Home](./../..)/[Facebook](./..)/[Medium](./)/Range_Sum_Query_Mutable
<h1>Range Sum Query - Mutable</h1>

<p>
Given an integer array nums, handle multiple queries of the following types:

1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
                                                                                                         
Implement the NumArray class:

* NumArray(int[] nums) Initializes the object with the integer array nums.
* void update(int index, int val) Updates the value of nums[index] to be val.
* int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
                                                                                                         
</p>

<b>Example 1:</b>

    Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]

    Explanation
    NumArray numArray = new NumArray([1, 3, 5]);
    numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
    numArray.update(1, 2);   // nums = [1, 2, 5]
    numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- 0 <= index < nums.length
- -100 <= val <= 100
- 0 <= left <= right < nums.length
- At most 3 * 104 calls will be made to update and sumRange.

<h2>Solution</h2>

```python
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = sum(nums)


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if val >= self.nums[index]:
            self.sums += (val - self.nums[index])
        else:
            self.sums -= (self.nums[index] - val)
        self.nums[index] = val


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        left_sum = sum(self.nums[:left])
        right_sum = sum(self.nums[right + 1:])
        return self.sums - left_sum - right_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```
