# [Home](./../..)/[Google](./..)/[Medium](./)/Car_Pooling
<h1>Car Pooling</h1>

<p>
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
</p>
<p>
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
</p>
<p>
Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 
</p>

<b>Example 1:</b>

    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

<b>Example 2:</b>

    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true

<b>Example 3:</b>

    Input: trips = [[2,1,5],[3,5,7]], capacity = 3
    Output: true

<b>Example 4:</b>

    Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
    Output: true

<b>Constraints:</b>

- trips.length <= 1000
- trips[i].length == 3
- 1 <= trips[i][0] <= 100
- 0 <= trips[i][1] < trips[i][2] <= 1000
- 1 <= capacity <= 100000
<h2>Solution</h2>

```python
# O(NlogN)
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # flat_list = []
        # for trip in trips:
        #     flat_list.append([trip[1],trip[0],0])
        #     flat_list.append([trip[2],trip[0],1])
        # flat_list.sort(key=lambda x:(x[0],-x[2],x[1]))
        # cap = 0
        # for ele in flat_list:
        #     if ele[2] == 0:
        #         cap+=ele[1]
        #     else:
        #         cap-=ele[1]
        #     if cap>capacity:
        #         return False
        # return True
# O(N)        
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
```
