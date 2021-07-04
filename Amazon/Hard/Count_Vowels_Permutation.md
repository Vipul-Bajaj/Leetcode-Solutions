# [Home](./../..)/[Amazon](./..)/[Hard](./)/Count_Vowels_Permutation
<h1>Count Vowels Permutation</h1>

<p>
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
</p>

- Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
- Each vowel 'a' may only be followed by an 'e'.
- Each vowel 'e' may only be followed by an 'a' or an 'i'.
- Each vowel 'i' may not be followed by another 'i'.
- Each vowel 'o' may only be followed by an 'i' or a 'u'.
- Each vowel 'u' may only be followed by an 'a'.

<p>
Since the answer may be too large, return it modulo 10^9 + 7.
</p>

<b>Example 1:</b>

    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
    
<b>Example 2:</b>

    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
    
<b>Example 3:</b>

    Input: n = 5
    Output: 68

<b>Constraints:</b>

- 1 <= n <= 2 * 10^4

<h2>Solution</h2>

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a=e=o=i=u=1
        mod = 10**9+7
        for l in range(1,n):
            na = (e+i+u)%mod
            ne = (a+i)%mod
            ni = (e+o)%mod
            no = (i)%mod
            nu = (i+o)%mod
            a,e,i,o,u = na,ne,ni,no,nu
        return (a+e+i+o+u)%mod
```
