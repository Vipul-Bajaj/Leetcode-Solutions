# [Home](./../..)/[Amazon](./..)/[Easy](./)/Sum_of_All_Subset_XOR_Totals
<h1>Sum of All Subset XOR Totals</h1>

<p>
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
</p>

* For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
<p>
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
</p>

<b>Example 1:</b>

    Input: nums = [1,3]
    Output: 6
    Explanation: The 4 subsets of [1,3] are:
    - The empty subset has an XOR total of 0.
    - [1] has an XOR total of 1.
    - [3] has an XOR total of 3.
    - [1,3] has an XOR total of 1 XOR 3 = 2.
    0 + 1 + 3 + 2 = 6
    
<b>Example 2:</b>

    Input: nums = [5,1,6]
    Output: 28
    Explanation: The 8 subsets of [5,1,6] are:
    - The empty subset has an XOR total of 0.
    - [5] has an XOR total of 5.
    - [1] has an XOR total of 1.
    - [6] has an XOR total of 6.
    - [5,1] has an XOR total of 5 XOR 1 = 4.
    - [5,6] has an XOR total of 5 XOR 6 = 3.
    - [1,6] has an XOR total of 1 XOR 6 = 7.
    - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
    0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

<b>Constraints:</b>

- 1 <= nums.length <= 12
- 1 <= nums[i] <= 20

<h2>Solution</h2>

```python
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def bt(nums, index, running_xor):
            nonlocal ans
            if index >= len(nums):
                ans += running_xor
            else:
                bt(nums, index+1, nums[index]^running_xor)
                bt(nums, index+1, running_xor)
                
        bt(nums, 0, 0)
        return ans
```
