# [Home](./../..)/[Amazon](./..)/[Easy](./)/Majority_Element
<h1>Majority Element</h1>

<p>
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

</p>

<b>Example 1:</b>

    Input: nums = [3,2,3]
    Output: 3
    
<b>Example 2:</b>

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

<b>Constraints:</b>

- n == nums.length
- 1 <= n <= 5 * 104
- -231 <= nums[i] <= 231 - 1

<h2>Solution</h2>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for i in nums:
            if cand is None or count == 0:
                cand = i
                count+=1
            elif cand == i:
                count+=1
            else:
                count-=1
        return cand
```
