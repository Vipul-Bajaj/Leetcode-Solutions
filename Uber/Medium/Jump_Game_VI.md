# [Home](./../..)/[Uber](./..)/[Medium](./)/Jump_Game_VI
<h1>Jump Game VI</h1>

<p>
You are given a 0-indexed integer array nums and an integer k.
</p>
<p>
You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
</p>
<p>
You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
</p>
<p>
Return the maximum score you can get.
</p>

<b>Example 1:</b>

    Input: nums = [1,-1,-2,4,-7,3], k = 2
    Output: 7
    Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
    
<b>Example 2:</b>

    Input: nums = [10,-5,-2,4,0,3], k = 3
    Output: 17
    Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
    
<b>Example 3:</b>

    Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
    Output: 0

<b>Constraints:</b>

- 1 <= nums.length, k <= 105
- -104 <= nums[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float("inf")]*n
        dp[0] = nums[0]
        heap = []
        heapq.heappush(heap,(-nums[0],0))
        for i in range(1,n):
            while heap[0][1]<i-k:
                heapq.heappop(heap)
            dp[i] = dp[heap[0][1]]+nums[i]
            heapq.heappush(heap,(-dp[i],i))
        return dp[n-1]
```
