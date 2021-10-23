# [Home](./../..)/[Google](./..)/[Medium](./)/Minimum_Number_of_Days_to_Make_m_Bouquets
<h1>Minimum Number of Days to Make m Bouquets</h1>

<p>
Given an integer array bloomDay, an integer m and an integer k.
</p>
<p>
We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
</p>
<p>
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
</p>
<p>
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
</p>

<b>Example 1:</b>

    Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
    Output: 3
    Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
    We need 3 bouquets each should contain 1 flower.
    After day 1: [x, _, _, _, _]   // we can only make one bouquet.
    After day 2: [x, _, _, _, x]   // we can only make two bouquets.
    After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

<b>Example 2:</b>

    Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
    Output: -1
    Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

<b>Example 3:</b>

    Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
    Output: 12
    Explanation: We need 2 bouquets each should have 3 flowers.
    Here's the garden after the 7 and 12 days:
    After day 7: [x, x, x, x, _, x, x]
    We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
    After day 12: [x, x, x, x, x, x, x]
    It is obvious that we can make two bouquets in different ways.

<b>Example 4:</b>

    Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
    Output: 1000000000
    Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.

<b>Example 5:</b>

    Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
    Output: 9
    
<b>Constraints:</b>

- bloomDay.length == n
- 1 <= n <= 10^5
- 1 <= bloomDay[i] <= 10^9
- 1 <= m <= 10^6
- 1 <= k <= n

<h2>Solution</h2>

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k>n:
            return -1
        left, right = 1, max(bloomDay)
        
        while left<right:
            mid = left + (right-left)//2
            
            flowers = bouquets = 0
            for bloomingDay in bloomDay:
                flowers = 0 if bloomingDay>mid else flowers+1
                if flowers >=k:
                    flowers = 0
                    bouquets+=1
                if bouquets == m:
                    break
            
            if bouquets>=m:
                right = mid
            else:
                left=mid+1
        
        return left
```
