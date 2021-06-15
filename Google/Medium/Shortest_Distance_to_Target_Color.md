# [Home](./../..)/[Google](./..)/[Medium](./)/Shortest_Distance_to_Target_Color
<h1>Shortest Distance to Target Color</h1>

<p>
You are given an array colors, in which there are three colors: 1, 2 and 3.
</p>
<p>
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.
</p>

<b>Example 1:</b>

    Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
    Output: [3,0,3]
    Explanation: 
    The nearest 3 from index 1 is at index 4 (3 steps away).
    The nearest 2 from index 2 is at index 2 itself (0 steps away).
    The nearest 1 from index 6 is at index 3 (3 steps away).
    
<b>Example 2:</b>

    Input: colors = [1,2], queries = [[0,3]]
    Output: [-1]
    Explanation: There is no 3 in the array.
    
<b>Constraints:</b>

- 1 <= colors.length <= 5*10^4
- 1 <= colors[i] <= 3
- 1 <= queries.length <= 5*10^4
- queries[i].length == 2
- 0 <= queries[i][0] < colors.length
- 1 <= queries[i][1] <= 3

<h2>Solution</h2>

```python
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        colors_map = defaultdict(list)
        for idx,color in enumerate(colors):
            colors_map[color].append(idx)
        out = []            
        for idx,color in queries:
            if len(colors_map[color])==0:
                out.append(-1)
                continue
            in_idx = bisect_left(colors_map[color],idx)
            left = abs(colors_map[color][max(in_idx-1,0)]-idx)
            right = abs(colors_map[color][min(in_idx,len(colors_map[color])-1)]-idx)
            out.append(min(left,right))
        return out
```
