# [Home](./../..)/[Amazon](./..)/[Medium](./)/Frequency_of_the_Most_Frequent_Element
<h1>Frequency of the Most Frequent Element</h1>

<p>
The frequency of an element is the number of times it occurs in an array.
</p>
<p>
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
</p>
<p>
Return the maximum possible frequency of an element after performing at most k operations.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,4], k = 5
    Output: 3
    Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
    4 has a frequency of 3.

<b>Example 2:</b>

    Input: nums = [1,4,8,13], k = 5
    Output: 2
    Explanation: There are multiple optimal solutions:
    - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
    - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
    - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

<b>Example 3:</b>

    Input: nums = [3,9,6], k = 2
    Output: 1

<b>Constraints:</b>

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105
- 1 <= k <= 105

<h2>Solution</h2>

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
```
