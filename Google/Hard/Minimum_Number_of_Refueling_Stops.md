# [Home](./../../..)/[Google](./../..)/[Hard](./..)/Minimum_Number_of_Refueling_Stops
<h1>Minimum Number of Refueling Stops</h1>

<p>
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

</p>

<b>Example 1:</b>

    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.
    
<b>Example 2:</b>

    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can't reach the target (or even the first gas station).
    
<b>Example 3:</b>

    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: 
    We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.

<b>Constraints:</b>

- 1 <= target, startFuel, stations[i][1] <= 10^9
- 0 <= stations.length <= 500
- 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

<h2>Solution</h2>

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q = []
        stations.append([target,2**31])
        refuel= prev =0
        for loc,cap in stations:
            startFuel-= loc-prev
            while q and startFuel < 0:
                startFuel += -1*heapq.heappop(q)
                refuel+=1
            if startFuel<0:
                return -1
            heapq.heappush(q,-cap)
            prev = loc
        return refuel
```
