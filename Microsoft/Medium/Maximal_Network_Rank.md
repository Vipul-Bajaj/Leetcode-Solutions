# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Maximal_Network_Rank
<h1>Maximal Network Rank</h1>

<p>
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
</p>
<p>
The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
</p>
<p>
The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
</p>
<p>
Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/ex1.png">

    Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
    Output: 4
    Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/21/ex2.png">

    Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    Output: 5
    Explanation: There are 5 roads that are connected to cities 1 or 2.

<b>Example 3:</b>

    Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    Output: 5
    Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
    
<b>Constraints:</b>

- 2 <= n <= 100
- 0 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 2
- 0 <= ai, bi <= n-1
- ai != bi
- Each pair of cities has at most one road connecting them.

<h2>Solution</h2>

```python
class Solution:
    def isConnected(self,x,y, hash_map):
        return y in hash_map[x]
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0]*n
        hash_map = defaultdict(list)
        
        for x,y in roads:
            degrees[x]+=1
            degrees[y]+=1
            hash_map[x].append(y)
            hash_map[y].append(x)
        
        max_rank = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                max_rank=max(max_rank,degrees[i]+degrees[j]-self.isConnected(i,j,hash_map))
        return max_rank
```
