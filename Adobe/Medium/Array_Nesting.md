# [Home](./../..)/[Adobe](./..)/[Medium](./)/Array_Nesting
<h1>Array Nesting</h1>

<p>
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
</p>
<p>
You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
</p>
- The first element in s[k] starts with the selection of the element nums[k] of index = k.
- The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
- We stop adding right before a duplicate element occurs in s[k].

<p>
Return the longest length of a set s[k].
</p>

<b>Example 1:</b>

    Input: nums = [5,4,0,3,1,6,2]
    Output: 4
    Explanation: 
    nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
    One of the longest sets s[k]:
    s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

<b>Example 2:</b>

    Input: nums = [0,1,2]
    Output: 1
    
<b>Constraints:</b>

- 1 <= nums.length <= 105
- 0 <= nums[i] < nums.length
- All the values of nums are unique.

<h2>Solution</h2>

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        l = 0
        for i,k in enumerate(nums):
            if nums[i]!=float('inf'):
                start = k
                c = 0
                while nums[start]!=float('inf'):
                    c+=1
                    nums[start],start = float('inf'),nums[start]
                    
                l = max(l,c)
        return l
```
