# [Home](./../..)/[Amazon](./..)/[Medium](./)/Decode_XORed_Permutation
<h1>Decode XORed Permutation</h1>

<p>
There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.
<br>
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].
<br>
Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.
</p>

<b>Example 1:</b>

    Input: encoded = [3,1]
    Output: [1,2,3]
    Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
    
<b>Example 2:</b>

    Input: encoded = [6,5,4,6]
    Output: [2,4,1,5,3]
    
<b>Constraints:</b>

- 3 <= n < 105
- n is odd.
- encoded.length == n - 1

<h2>Solution</h2>

```python
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)+1
        perm = [0]*n
        x = 0
        for i in range(1,n+1):
            x^=i
        perm[0]^=x    
        for i in range(1,n-1,2):
            perm[0]^=encoded[i]
        for i in range(1,n):
            perm[i] = perm[i-1]^encoded[i-1]
        return perm
```
