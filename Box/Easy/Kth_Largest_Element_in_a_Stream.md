# [Home](./../..)/[Box](./..)/[Easy](./)/Kth_Largest_Element_in_a_Stream
<h1>Kth Largest Element in a Stream</h1>

<p>
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
</p>
<p>
Implement KthLargest class:
</p>

- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

<b>Example 1:</b>

    Input
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

    Explanation
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);   // return 4
    kthLargest.add(5);   // return 5
    kthLargest.add(10);  // return 5
    kthLargest.add(9);   // return 8
    kthLargest.add(4);   // return 8
 
<b>Constraints:</b>

* 1 <= k <= 104
* 0 <= nums.length <= 104
* -104 <= nums[i] <= 104
* -104 <= val <= 104
* At most 104 calls will be made to add.
* It is guaranteed that there will be at least k elements in the array when you search for the kth element.

<h2>Solution</h2>

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for num in nums:
            heapq.heappush(self.heap,num)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
             
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
            return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
