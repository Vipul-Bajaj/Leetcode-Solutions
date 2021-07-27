# [Home](./../..)/[Facebook](./..)/[Easy](./)/Sum_of_Unique_Elements
<h1>Sum of Unique Elements</h1>

<p>
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
</p>
<p>
Return the sum of all the unique elements of nums.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,2]
    Output: 4
    Explanation: The unique elements are [1,3], and the sum is 4.

<b>Example 2:</b>

    Input: nums = [1,1,1,1,1]
    Output: 0
    Explanation: There are no unique elements, and the sum is 0.

<b>Example 3:</b>

    Input: nums = [1,2,3,4,5]
    Output: 15
    Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

<b>Constraints:</b>

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

<h2>Solution</h2>

```python
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        s = 0
        for k,v in count.items():
            if v == 1:
                s+=k
        return s
```
