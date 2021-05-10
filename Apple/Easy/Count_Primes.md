# [Home](./../..)/[Apple](./..)/[Easy](./)/Count_Primes
<h1>Count Primes</h1>

<p>
Count the number of prime numbers less than a non-negative number, n.
</p>

<b>Example 1:</b>

    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    
<b>Example 2:</b>

    Input: n = 0
    Output: 0

<b>Constraints:</b>

- 0 <= n <= 5 * 106

<h2>Solution</h2>

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n == 1:
            return 0
        primes = [True]*(n)
        primes[0],primes[1] = False,False
        count = 0
        for i in range(2,n):
            if primes[i]:
                primes[i] = True
                count+=1
                j = i*2
                while j<n:
                    primes[j] = False
                    j+=i
        return count
```
