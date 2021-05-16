# [Home](./../..)/[Twiiter](./..)/[Medium](./)/K_diff_Pairs_in_an_Array
<h1>K-diff Pairs in an Array</h1>

<p>
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
</p>

* 0 <= i < j < nums.length
* |nums[i] - nums[j]| == k

<p>
Notice that |val| denotes the absolute value of val.

</p>

<b>Example 1:</b>

    Input: nums = [3,1,4,1,5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
    
<b>Example 2:</b>

    Input: nums = [1,2,3,4,5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    
<b>Example 3:</b>

    Input: nums = [1,3,1,5,4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).
    
<b>Example 4:</b>

    Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
    Output: 2

<b>Constraints:</b>

- 1 <= nums.length <= 104
- -107 <= nums[i] <= 107
- 0 <= k <= 107

<h2>Solution</h2>

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        count = Counter(nums)
        
        for num in count:
            if k>0 and num+k in count:
                res+=1
            elif k ==0 and count[num]>1:
                res+=1
        return res
```
