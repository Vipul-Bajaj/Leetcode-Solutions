# [Home](./../..)/[Google](./..)/[Medium](./)/Maximum_Points_You_Can_Obtain_from_Cards
<h1>Maximum Points You Can Obtain from Cards</h1>

<p>
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
</p>

<b>Example 1:</b>

    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
    
<b>Example 2:</b>

    Input: cardPoints = [2,2,2], k = 2
    Output: 4
    Explanation: Regardless of which two cards you take, your score will always be 4.
    
<b>Example 3:</b>

    Input: cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55
    Explanation: You have to take all the cards. Your score is the sum of points of all cards.

<b>Example 4:</b>

    Input: cardPoints = [1,1000,1], k = 1
    Output: 1
    Explanation: You cannot take the card in the middle. Your best score is 1. 
    
<b>Example 5:</b>

    Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
    Output: 202
    
<b>Constraints:</b>

- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length

<h2>Solution</h2>

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        i = 0
        j = n-k
        total = sum(cardPoints[j:])
        best = total
        for i in range(k):
            total += cardPoints[i] - cardPoints[j]
            best = max(best,total)
            i+=1
            j+=1
        return best
```
