# [Home](./../..)/[Google](./..)/[Medium](./)/Water_and_Jug_Problem
<h1>Water and Jug Problem</h1>

<p>
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

- Fill any of the jugs with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

</p>

<b>Example 1:</b>

    Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
    Output: true
    Explanation: The famous Die Hard example 
    
<b>Example 2:</b>

    Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
    Output: false
    
<b>Example 3:</b>

    Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
    Output: true
    
<b>Constraints:</b>

- 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106

<h2>Solution</h2>

```python
class Solution:
    def gcd(self,a,b):
        while b!=0:
            a,b = b,a%b
        return a
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False
        if targetCapacity == jug1Capacity or targetCapacity == jug1Capacity or targetCapacity == 0:
            return True
        gcd = self.gcd(jug1Capacity,jug2Capacity) if jug1Capacity>jug2Capacity else self.gcd(jug2Capacity,jug1Capacity)
        return targetCapacity%gcd == 0
```
