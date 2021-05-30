# [Home](./../..)/[Amazon](./..)/[Hard](./)/Maximum_Gap
<h1>Maximum Gap</h1>

<p>
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
</p>
<p>
You must write an algorithm that runs in linear time and uses linear extra space.
</p>

<b>Example 1:</b>

    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
  
<b>Example 2:</b>

    Input: nums = [10]
    Output: 0
    Explanation: The array contains less than 2 elements, therefore return 0.

<b>Constraints:</b>

- 1 <= nums.length <= 104
0 <= nums[i] <= 109

<h2>Solution</h2>

```python
class Bucket:
    def __init__(self):
        self.used = False
        self.min = 2**31
        self.max = -2**31
    def __repr__(self):
        return repr("["+self.used+", "+ self.min + ", " + self.max+ "]")
    def __str__(self):
        return "["+str(self.used)+", "+ str(self.min) + ", " + str(self.max)+ "]"
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n<2:
            return 0
        
        min_v = min(nums)
        max_v = max(nums)
        
        bucket_size = max(1,(max_v-min_v)//(n-1))
        bucket_num = ((max_v-min_v)//bucket_size) + 1
        
        buckets = [Bucket() for i in range(bucket_num)]
        
        for num in nums:
            bucket_idx = (num-min_v)//bucket_size
            buckets[bucket_idx].used = True
            buckets[bucket_idx].min = min(buckets[bucket_idx].min,num)
            buckets[bucket_idx].max = max(buckets[bucket_idx].max,num)
            
        prev_bucket_min = min_v
        max_gap = 0
        for bucket in buckets:
            # print(bucket)
            if not bucket.used:
                continue
            max_gap = max(max_gap,bucket.min-prev_bucket_min)
            prev_bucket_min = bucket.max
        return max_gap
```
