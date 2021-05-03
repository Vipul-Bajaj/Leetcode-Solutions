# [Home](./../../..)/[Amazon](./../..)/[Medium](./..)/Top_K_Frequent_Elements
<h1>Top K Frequent Elements</h1>

<p>
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

</p>

<b>Example 1:</b>

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
<b>Example 2:</b>

    Input: nums = [1], k = 1
    Output: [1]

<b>Constraints:</b>

- 1 <= nums.legth <= 105
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

<h2>Solution</h2>

```python
import random
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

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

        n = len(unique)

        quickselect(0, n - 1, n - k)
        return unique[n - k:]
```
