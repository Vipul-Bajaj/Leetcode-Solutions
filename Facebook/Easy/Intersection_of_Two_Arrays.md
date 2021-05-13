# [Home](./../..)/[Facebook](./..)/[Easy](./)/Intersection_of_Two_Arrays
<h1>Intersection of Two Arrays</h1>

<p>
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
</p>

<b>Example 1:</b>

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
    
<b>Example 2:</b>

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

<b>Constraints:</b>

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        if m<n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        out = []
        count = Counter(nums1)
        for i in nums2:
            if count[i]>0:
                out.append(i)
                count[i]=0
        return out
```
