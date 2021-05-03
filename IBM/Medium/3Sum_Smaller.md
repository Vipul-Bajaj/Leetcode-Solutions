# [Home](./../../..)/[IBM](./../..)/[Medium](./..)/3Sum_Smaller
# [Home](./../../..)/[IBM](./../..)/[Medium](./..)/3Sum_Smaller
<h1>3Sum Smaller</h1>

<p>
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?

</p>

<b>Example 1:</b>

    Input: nums = [-2,0,1,3], target = 2
    Output: 2
    Explanation: Because there are two triplets which sums are less than 2:
    [-2,0,1]
    [-2,0,3]
    
<b>Example 2:</b>

    Input: nums = [], target = 0
    Output: 0

<b>Example 3:</b>

    Input: nums = [0], target = 0
    Output: 0

<b>Constraints:</b>

- n == nums.length
- 0 <= n <= 300
- -100 <= nums[i] <= 100
- -100 <= target <= 100

<h2>Solution</h2>

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n-2):
            # if nums[i]>=target:
            #     break
            j = i+1
            k = n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] < target:
                    count+=k-j
                    j+=1
                else:
                    k-=1
        
        return count
```
