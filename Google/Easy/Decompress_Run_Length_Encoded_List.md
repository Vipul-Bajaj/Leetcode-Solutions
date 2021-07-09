# [Home](./../..)/[Google](./..)/[Easy](./)/Decompress_Run_Length_Encoded_List
<h1>Decompress Run-Length Encoded List</h1>

<p>
We are given a list nums of integers representing a list compressed with run-length encoding.
<br>
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
<br>
Return the decompressed list.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,4]
    Output: [2,4,4,4]
    Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
    The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
    At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
    
<b>Example 2:</b>

    Input: nums = [1,1,2,3]
    Output: [1,3,3]

<b>Constraint:</b>
- 2 <= nums.length <= 100
- nums.length % 2 == 0
- 1 <= nums[i] <= 100

<h2>Solution</h2>

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0,len(nums),2):
            out.extend(nums[i]*[nums[i+1]])
        return out
```
