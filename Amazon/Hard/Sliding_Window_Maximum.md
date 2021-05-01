<h1>Sliding Window Maximum</h1>

<p>
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

</p>

<b>Example 1:</b>

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    
<b>Example 2:</b>

    Input: nums = [1], k = 1
    Output: [1]
    
<b>Example 3:</b>

    Input: nums = [1,-1], k = 1
    Output: [1,-1]

<b>Example 4:</b>

    Input: nums = [9,11], k = 2
    Output: [11]

<b>Example 5:</b>

    Input: nums = [4,-2], k = 2
    Output: [4]

<b>Constraints:</b>

- 1 <= nums.length <= 105
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

<h2>Solution</h2>

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        ans = []
        for i in range(k): 
        	
        	while q and nums[i] >= nums[q[-1]] : 
        		q.pop() 
        	
        	q.append(i); 
        	
        for i in range(k, n): 
        	
        	ans.append(nums[q[0]])
        	while q and q[0] <= i-k: 
        		q.popleft() 
        
        	while q and nums[i] >= nums[q[-1]] : 
        		q.pop() 
        	
        	q.append(i) 
        
        ans.append(nums[q[0]])
        
        return ans
```
