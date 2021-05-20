# [Home](./../..)/[Facebook](./..)/[Medium](./)/Dot_Product_of_Two_Sparse_Vectors
<h1>Dot Product of Two Sparse Vectors</h1>

<p>
Given two sparse vectors, compute their dot product.

Implement class SparseVector:
</p>

* SparseVector(nums) Initializes the object with the vector nums
* dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

<p>
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

<b>Follow up:</b> What if only one of the vectors is sparse?
</p>

<b>Example 1:</b>

    Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    Output: 8
    Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
    
<b>Example 2:</b>

    Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
    Output: 0
    Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

<b>Constraints:</b>

- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 0 <= nums1[i], nums2[i] <= 100

<h2>Solution</h2>

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.hash_map = {}
        for i,n in enumerate(nums):
            if n!=0:
                self.hash_map[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for i,n in self.hash_map.items():
            if i in vec.hash_map:
                prod+= n*vec.hash_map[i]
        return prod
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```
