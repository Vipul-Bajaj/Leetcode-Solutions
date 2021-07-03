# [Home](./../..)/[Google](./..)/[Easy](./)/Guess_Number_Higher_or_Lower
<h1>Guess Number Higher or Lower</h1>

<p>
We are playing the Guess Game. The game is as follows:
</p>
<p>
I pick a number from 1 to n. You have to guess which number I picked.
</p>
<p>
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
</p>
<p>
You call a pre-defined API int guess(int num), which returns 3 possible results:
</p>

- -1: The number I picked is lower than your guess (i.e. pick < num).
- 1: The number I picked is higher than your guess (i.e. pick > num).
- 0: The number I picked is equal to your guess (i.e. pick == num).

<p>
Return the number that I picked.
</p>

<b>Example 1:</b>

    Input: n = 10, pick = 6
    Output: 6
    
<b>Example 2:</b>

    Input: n = 1, pick = 1
    Output: 1
    
<b>Example 3:</b>

    Input: n = 2, pick = 1
    Output: 1
    
<b>Example 4:</b>

    Input: n = 2, pick = 2
    Output: 2    

<b>Note:</b>
- 1 <= n <= 231 - 1
- 1 <= pick <= n


<h2>Solution</h2>

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
# # Binary search
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l,h = 1,n
#         while l<=h:
#             mid = (l+h)//2
#             g = guess(mid)
#             if g == 0:
#                 return mid
#             elif g == -1:
#                 h = mid-1
#             else:
#                 l = mid+1
# Ternary Search
class Solution:
    def guessNumber(self, n: int) -> int:
        l,h = 1,n
        while l<=h:
            m1 = l+((h-l)//3)
            m2 = h-((h-l)//3)
            g1 = guess(m1)
            g2 = guess(m2)
            if g1 == 0:
                return m1
            elif g2 == 0:
                return m2
            elif g1<0:
                h = m1-1
            elif g2>0:
                l = m2+1
            else:
                l = m1+1
                h = m2-1
```
