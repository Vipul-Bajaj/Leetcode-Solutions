# [Home](./../..)/[Amazon](./..)/[Medium](./)/Length_of_Longest_Fibonacci_Subsequence
<h1>Length of Longest Fibonacci Subsequence</h1>

<p>
A sequence X1, X2, ..., Xn is Fibonacci-like if:
</p>

* n >= 3
* Xi + Xi+1 = Xi+2 for all i + 2 <= n
<p>
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
</p>
<p>
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
</p>

<b>Example 1:</b>

    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    
<b>Example 2:</b>

    Input: arr = [1,3,7,11,12,14,18]
    Output: 3
    Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

<b>Constraints:</b>

- 3 <= arr.length <= 1000
- 1 <= arr[i] < arr[i + 1] <= 109

<h2>Solution</h2>

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x:i for i,x in enumerate(arr)}
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for k, z in enumerate(arr):
            for j in range(k):
                i = index.get(z - arr[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
```
