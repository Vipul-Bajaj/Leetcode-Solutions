# [Home](./../..)/[Amazon](./..)/[Easy](./)/Fair_Candy_Swap

<h1>Fair Candy Swap</h1>

<p>
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
</p>
<p>
Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.
</p>
<p>
Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.
</p>

<b>Example 1:</b>

    Input: aliceSizes = [1,1], bobSizes = [2,2]
    Output: [1,2]

<b>Example 2:</b>

    Input: aliceSizes = [1,2], bobSizes = [2,3]
    Output: [1,2]

<b>Example 3:</b>

    Input: aliceSizes = [2], bobSizes = [1,3]
    Output: [2,3]

<b>Example 4:</b>

    Input: aliceSizes = [1,2,5], bobSizes = [2,4]
    Output: [5,4]

<b>Constraints:</b>

- 1 <= aliceSizes.length, bobSizes.length <= 104
- 1 <= aliceSizes[i], bobSizes[j] <= 105
- Alice and Bob have a different total number of candies.
- There will be at least one valid answer for the given input.

<h2>Solution</h2>

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sa,sb = sum(aliceSizes),sum(bobSizes)
        bob = set(bobSizes)
        for x in aliceSizes:
            if x + (sb-sa)//2 in bob:
                return [x, x + (sb-sa)//2]
```
