# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Remove_Duplicates_from_Sorted_Array_II
<h1>Remove Duplicates from Sorted Array II</h1>

<p>
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
</p>
<p>
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
</p>
<p>
Clarification:
</p>
<p>
Confused why the returned value is an integer, but your answer is an array?
</p>
<p>
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller.
</p>
<p>
Internally you can think of this:
</p>

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

<b>Example 1:</b>

    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3]
    Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
    
<b>Example 2:</b>

    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3]
    Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.

<b>Constraints:</b>

- 1 <= nums.length <= 3 * 104
- -104 <= nums[i] <= 104
- nums is sorted in ascending order.

<h2>Solution</h2>

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for idx, val in enumerate(nums):
            if (length <= 1) or (nums[length - 2] != val):
                nums[length] = val
                length += 1
        return length
```
