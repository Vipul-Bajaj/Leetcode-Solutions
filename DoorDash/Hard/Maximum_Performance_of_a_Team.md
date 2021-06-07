# [Home](./../..)/[DoorDash](./..)/[Hard](./)/Maximum_Performance_of_a_Team
<h1>Maximum Performance of a Team</h1>

<p>
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
</p>
<p>
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
</p>
<p>
The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
</p>
<p>
Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.
</p>

<b>Example 1:</b>

    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
    Output: 60
    Explanation: 
    We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
    
<b>Example 2:</b>

    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
    Output: 68
    Explanation:
    This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

<b>Example 3:</b>

    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
    Output: 72
    
<b>Constraints:</b>

- 1 <= <= k <= n <= 105
- speed.length == n
- efficiency.length == n
- 1 <= speed[i] <= 105
- 1 <= efficiency[i] <= 108

<h2>Solution</h2>

```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = list(zip(efficiency,speed))
        candidates.sort(key=lambda x:-x[0])
        # print(eff_speed)
        team = 0
        speed_heap = []
        speed_sum = 0
        for curr_eff, curr_speed in candidates:
            if len(speed_heap)>k-1:
                speed_sum-=heapq.heappop(speed_heap)
            
            heapq.heappush(speed_heap,curr_speed)
            
            speed_sum+=curr_speed
            team = max(team,curr_eff*speed_sum)
        return team%((10**9)+7)
```