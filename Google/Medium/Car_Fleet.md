# [Home](./../..)/[Google](./..)/[Medium](./)/Car_Fleet
<h1>Car Fleet</h1>

<p>
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
</p>
<p>
You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
</p>
<p>
A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
</p>
<p>
The distance between these two cars is ignored (i.e., they are assumed to have the same position).
</p>
<p>
A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
</p>
<p>
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
</p>
<p>
Return the number of car fleets that will arrive at the destination.
</p>

<b>Example 1:</b>

    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3
    Explanation: 
    The cars starting at 10 and 8 become a fleet, meeting each other at 12.
    The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
    The cars starting at 5 and 3 become a fleet, meeting each other at 6.
    Note that no other cars meet these fleets before the destination, so the answer is 3.

<b>Example 2:</b>

    Input: target = 10, position = [3], speed = [3]
    Output: 1


<b>Constraints:</b>

- n == position.length == speed.length
- 1 <= n <= 105
- 0 < target <= 106
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 106

<h2>Solution</h2>

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-p)/s for p,s in sorted(zip(position,speed),)]
        
        print(time)
        res = 0
        curr = 0
        for t in time[::-1]:
            if t>curr:
                res+=1
                curr = t
        return res
```
