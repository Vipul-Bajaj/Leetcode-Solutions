# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Kth_Largest_Element_in_an_Array
# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Kth_Largest_Element_in_an_Array
<h1>Kth Largest Element in an Array</h1>

<p>
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

</p>

<b>Example 1:</b>

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    
<b>Example 2:</b>

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

<b>Constraints:</b>

- 1 <= k <= nums.length <= 104
- -10^4 <= nums[i] <= 10^4

<h2>Solution</h2>

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # k_large = heapq.nlargest(k,nums)
        # return k_large[-1]
        def partition(left, right, pivot_index) -> int:
            pivot_ele = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot_ele:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(nums)

        quickselect(0, n - 1, n - k)
        return nums[n - k]
```
