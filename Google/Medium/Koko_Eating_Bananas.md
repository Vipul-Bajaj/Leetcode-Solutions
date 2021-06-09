# [Home](./../..)/[Google](./..)/[Medium](./)/Koko_Eating_Bananas
<h1>Koko Eating Bananas</h1>

<p>
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
</p>
<p>
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
</p>
<p>
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
</p>
<p>
Return the minimum integer k such that she can eat all the bananas within h hours.
</p>

<b>Example 1:</b>

    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
<b>Example 2:</b>

    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

<b>Example 3:</b>

    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

<b>Constraints:</b>

- 1 <= piles.length <= 104
- piles.length <= h <= 109
- 1 <= piles[i] <= 109

<h2>Solution</h2>

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        while low<high:
            mid = (low+high)//2
            
            if sum((p-1)//mid+1 for p in piles)>h:
                low = mid+1
            else:
                high = mid
        return low
```
