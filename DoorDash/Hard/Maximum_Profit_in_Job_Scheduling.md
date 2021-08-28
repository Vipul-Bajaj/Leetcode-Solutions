# [Home](./../..)/[DoorDash](./..)/[Hard](./)/Maximum_Profit_in_Job_Scheduling
<h1>Maximum Profit in Job Scheduling</h1>

<p>
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
</p>
<p>
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
</p>
<p>
If you choose a job that ends at time X you will be able to start another job that starts at time X.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png">

    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    Explanation: The subset chosen is the first and fourth job. 
    Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/10/sample2_1584.png">

    Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    Output: 150
    Explanation: The subset chosen is the first, fourth and fifth job. 
    Profit obtained 150 = 20 + 70 + 60.

<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png">

    Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    Output: 6

<b>Constraints:</b>

- 1 <= startTime.length == endTime.length == profit.length <= 5 * 104
- 1 <= startTime[i] < endTime[i] <= 109
- 1 <= profit[i] <= 104

<h2>Solution</h2>

```python
class Solution:
    def findNext(self, startTime, last):
        start = 0
        end = len(startTime)-1
        nextInd = end+1
        
        while start<=end:
            mid = (start+end)//2
            
            if startTime[mid]>=last:
                nextInd = mid
                end = mid-1
            else:
                start = mid+1
        return nextInd
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for s,e,p in zip(startTime, endTime, profit):
            jobs.append([s,e,p])
        jobs.sort(key = lambda x:x[0])
        startTime.sort()
        n = len(jobs)
        dp = [0]*(n+1)
        
        for i in range(n-1,-1,-1):
            currProfit = 0
            nextInd = self.findNext(startTime, jobs[i][1])
            if nextInd != n:
                currProfit = jobs[i][2]+dp[nextInd]
            else:
                currProfit = jobs[i][2]

            if i == n-1:
                dp[i] = currProfit
            else:
                dp[i] = max(currProfit, dp[i+1])
        
        return dp[0]
```
