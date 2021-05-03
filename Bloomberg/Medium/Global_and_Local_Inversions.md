# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Global_and_Local_Inversions
<h1>Global and Local Inversions</h1>

<p>
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

</p>

<b>Example 1:</b>

    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local inversion.
    
<b>Example 2:</b>

    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local inversion.
 
<b>Constraints:</b>

    A will be a permutation of [0, 1, ..., A.length - 1].
    A will have length in range [1, 5000].
    The time limit for this problem has been reduced.

<h2>Solution</h2>

```python
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        max_value = -1
        for i in range(n-2):
            max_value = max(A[i],max_value)
            if max_value > A[i+2]:
                return False
        return True
```
