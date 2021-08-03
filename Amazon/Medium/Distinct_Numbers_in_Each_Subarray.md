# [Home](./../..)/[Amazon](./..)/[Medium](./)/Distinct_Numbers_in_Each_Subarray
<h1>Distinct Numbers in Each Subarray</h1>

<p>
Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].
</p>
<p>
Return the array ans.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,2,2,1,3], k = 3
    Output: [3,2,2,2,3]
    Explanation: The number of distinct elements in each subarray goes as follows:
    - nums[0:2] = [1,2,3] so ans[0] = 3
    - nums[1:3] = [2,3,2] so ans[1] = 2
    - nums[2:4] = [3,2,2] so ans[2] = 2
    - nums[3:5] = [2,2,1] so ans[3] = 2
    - nums[4:6] = [2,1,3] so ans[4] = 3

<b>Example 2:</b>

    Input: nums = [1,1,1,1,2,3,4], k = 4
    Output: [1,2,3,4]
    Explanation: The number of distinct elements in each subarray goes as follows:
    - nums[0:3] = [1,1,1,1] so ans[0] = 1
    - nums[1:4] = [1,1,1,2] so ans[1] = 2
    - nums[2:5] = [1,1,2,3] so ans[2] = 3
    - nums[3:6] = [1,2,3,4] so ans[3] = 4


<b>Constraints:</b>

- 1 <= k <= nums.length <= 105
- 1 <= nums[i] <= 105

<h2>Solution</h2>

```python
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        for i in nums[:k]:
            if i in ht:
                ht[i]+=1
            else:
                ht[i] = 1
        n = len(ht.keys())
        ans = [n]
        for i in range(k,len(nums)):
            if ht[nums[i-k]] == 1:
                del ht[nums[i-k]]
                n-=1
            else:
                ht[nums[i-k]]-=1
            if nums[i] not in ht:
                ht[nums[i]] = 1
                n+=1
            else:
                ht[nums[i]] += 1
            ans.append(n)
        return ans
```
