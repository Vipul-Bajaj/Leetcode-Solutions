# [Home](./../..)/[Amazon](./..)/[Medium](./)/Single_Element_in_a_Sorted_Array
<h1>Single Element in a Sorted Array</h1>

<p>
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

</p>

<b>Example 1:</b>

    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
    
<b>Example 2:</b>

    Input: nums = [3,3,7,7,10,11,11]
    Output: 10
    
<b>Constraints:</b>

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans ^ nums[i]
        return ans
```
