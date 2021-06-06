# [Home](./../..)/[Amazon](./..)/[Medium](./)/Capacity_To_Ship_Packages_Within_D_Days
<h1>Capacity To Ship Packages Within D Days</h1>

<p>
A conveyor belt has packages that must be shipped from one port to another within days days.
</p>
<p>
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
</p>
<p>
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
</p>

<b>Example 1:</b>

    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

    Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
    
<b>Example 2:</b>

    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6
    Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4
    
<b>Example 3:</b>

    Input: weights = [1,2,3,1,1], days = 4
    Output: 3
    Explanation:
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1
    
<b>Constraints:</b>

- 1 <= days <= weights.length <= 5 * 104
- 1 <= weights[i] <= 500

<h2>Solution</h2>

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights),sum(weights)
        while low<high:
            mid = (low+high)//2
            curr = 0
            d = 1
            for w in weights:
                if curr+w>mid:
                    d+=1
                    curr = 0
                curr+=w
            if d>days:
                low = mid+1
            else:
                high = mid
        return low
```
