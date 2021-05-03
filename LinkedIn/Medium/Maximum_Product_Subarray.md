<h1>Maximum Product Subarray</h1>

<p>
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

</p>

<b>Example 1:</b>

    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    
<b>Example 2:</b>

    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

<b>Constraints:</b>

- 1 <= nums.length <= 2 * 104
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

<h2>Solution</h2>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        minVal = nums[0]
        maxVal = nums[0]

        maxProduct = nums[0]

        for i in range(1, n, 1):

            if (nums[i] < 0):
                temp = maxVal
                maxVal = minVal
                minVal = temp

            maxVal = max(nums[i], maxVal * nums[i])
            minVal = min(nums[i], minVal * nums[i])

            maxProduct = max(maxProduct, maxVal)

        return maxProduct
```
