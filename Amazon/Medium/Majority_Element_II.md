# [Home](./../..)/[Amazon](./..)/[Medium](./)/Majority_Element_II
<h1>Majority Element II</h1>

<p>
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

</p>

<b>Example 1:</b>

    Input: nums = [3,2,3]
    Output: [3]
    
<b>Example 2:</b>

    Input: nums = [1]
    Output: [1]
    
<b>Example 3:</b>

    Input: nums = [1,2]
    Output: [1,2]

<b>Constraints:</b>

- 1 <= nums.length <= 5 * 104
- -109 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first_cand, second_cand = None,None
        first_count, second_count = 0,0
        for i in nums:
            if first_cand == i:
                first_count+=1
            elif second_cand == i:
                second_count+=1
            elif first_count == 0:
                first_cand = i
                first_count+=1
            elif second_count == 0:
                second_cand = i
                second_count+=1
            else:
                first_count-=1
                second_count-=1
        
        first_count, second_count = 0,0        
        for i in nums:
            if i == first_cand:
                first_count+=1
            elif i == second_cand:
                second_count += 1
        ans = []
        if first_count > math.floor(len(nums)/3):
            ans.append(first_cand)
        if second_count > math.floor(len(nums)/3):
            ans.append(second_cand)
        return ans
```
