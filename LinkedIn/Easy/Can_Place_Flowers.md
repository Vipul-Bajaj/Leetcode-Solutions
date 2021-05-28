# [Home](./../..)/[LinkedIn](./..)/[Easy](./)/Can_Place_Flowers
<h1>Can Place Flowers</h1>

<p>
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
</p>
<p>
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
</p>

<b>Example 1:</b>

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

<b>Example 2:</b>

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

<b>Constraints:</b>

- 1 <= flowerbed.length <= 2 * 104
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

<h2>Solution</h2>

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i<len(flowerbed):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n-=1
                flowerbed[i] = 1
            if n<=0:
                return True
            i+=1
        return False
```
