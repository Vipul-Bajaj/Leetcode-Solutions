# [Home](./../..)/[Amazon](./..)/[Easy](./)/Intersection_of_Two_Arrays_II
<h1>Intersection of Two Arrays II</h1>

<p>
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
</p>

<b>Example 1:</b>

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
    
<b>Example 2:</b>

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.

<b>Constraints:</b>

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

<b>Follow up:</b>

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        if m>n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        
        count1 = Counter(nums1)
        k = 0
        for i in nums2:
            if count1[i]>0:
                nums1[k] = i
                count1[i]-=1
                k+=1
        return nums1[:k]
```
