# [Home](./../..)/[Box](./..)/[Easy](./)/Number_of_1_Bits
<h1>Number of 1 Bits</h1>

<p>
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
<br>
Note:
</p>
* Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

<b>Example 1:</b>

    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
  
<b>Example 2:</b>

    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

<b>Example 3:</b>

    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
<b>Constraints:</b>

* The input must be a binary string of length 32.

<h2>Solution</h2>

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n!= 0 :
            c+=1
            n &= (n-1)
        return c
```
