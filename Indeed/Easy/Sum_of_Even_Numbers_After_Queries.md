# [Home](./../..)/[Indeed](./..)/[Easy](./)/Sum_of_Even_Numbers_After_Queries
<h1>Sum of Even Numbers After Queries</h1>

<p>
We have an array nums of integers, and an array queries of queries.
</p>
<p>
For the i-th query val = queries[i][0], index = queries[i][1], we add val to nums[index].  Then, the answer to the i-th query is the sum of the even values of A.
</p>
<p>
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array nums.)
</p>
<p>
Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
</p>

<b>Example 1:</b>

    Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]
    Explanation: 
    At the beginning, the array is [1,2,3,4].
    After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
    After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
    After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
    After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
    
<b>Constraint:</b>
- 1 <= nums.length <= 10000
- -10000 <= nums[i] <= 10000
- 1 <= queries.length <= 10000
- -10000 <= queries[i][0] <= 10000
- 0 <= queries[i][1] < nums.length

<h2>Solution</h2>

```python
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum([i for i in nums if i%2==0])
        ans = [0]*len(queries)
        i = 0
        for val,idx in queries:
            if nums[idx]%2 == 0:
                even-=nums[idx]
            nums[idx]+=val
            if nums[idx]%2==0:
                even+=nums[idx]
            ans[i] = even
            i+=1
        return ans
```
