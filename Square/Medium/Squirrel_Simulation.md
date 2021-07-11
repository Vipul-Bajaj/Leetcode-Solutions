# [Home](./../..)/[Square](./..)/[Medium](./)/Squirrel_Simulation
<h1>Squirrel Simulation</h1>

<p>
You are given two integers height and width representing a garden of size height x width. You are also given:
</p>

- an array tree where tree = [treer, treec] is the position of the tree in the garden,
- an array squirrel where squirrel = [squirrelr, squirrelc] is the position of the squirrel in the garden,
- and an array nuts where nuts[i] = [nutir, nutic] is the position of the ith nut in the garden.

<p>
The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.
</p>
<p>
Return the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one.
</p>
<p>
The distance is the number of moves.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/squirrel1-grid.jpg">

    Input: height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
    Output: 12
    Explanation: The squirrel should go to the nut at [2, 5] first to achieve a minimal distance.
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2021/04/24/squirrel2-grid.jpg">

    Input: height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
    Output: 3

<b>Constraint:</b>
- 1 <= height, width <= 100
- tree.length == 2
- squirrel.length == 2
- 1 <= nuts.length <= 5000
- nuts[i].length == 2
- 0 <= treer, squirrelr, nutir <= height
- 0 <= treec, squirrelc, nutic <= width

<h2>Solution</h2>

```python
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(point1,point2):
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
        total_dist = 0
        d = -2**31
        for nut in nuts:
            total_dist += dist(nut,tree)*2
            d = max(d,dist(nut,tree)-dist(nut,squirrel))
        return total_dist-d
```
