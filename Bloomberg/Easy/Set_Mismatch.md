# [Home](./../..)/[Bloomberg](./..)/[Easy](./)/Set_Mismatch
<h1>Set Mismatch</h1>

<p>
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
</p>
<p>
You are given an integer array nums representing the data status of this set after the error.
</p>
<p>
Find the number that occurs twice and the number that is missing and return them in the form of an array.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,2,4]
    Output: [2,3]
    
<b>Example 2:</b>

    Input: nums = [1,1]
    Output: [1,2]

<b>Constraints:</b>

- 2 <= nums.length <= 104
- 1 <= nums[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        miss = 1
        for n in nums:
            if nums[abs(n)-1]<0:
                dup = abs(n)
            else:
                nums[abs(n)-1]*=-1
        for i in range(1,len(nums)):
            if nums[i]>0:
                miss = i+1
        return [dup,miss]
```
