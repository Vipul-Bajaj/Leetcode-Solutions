# [Home](./../..)/[Amazon](./..)/[Medium](./)/Complex_Number_Multiplication
<h1>Complex Number Multiplication</h1>

<p>
A complex number can be represented as a string on the form "real+imaginaryi" where:
</p>

- real is the real part and is an integer in the range [-100, 100].
- imaginary is the imaginary part and is an integer in the range [-100, 100].
- i2 == -1.

<p>
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.
</p>

<b>Example 1:</b>

    Input: num1 = "1+1i", num2 = "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

<b>Example 2:</b>

    Input: num1 = "1+-1i", num2 = "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

<b>Constraints:</b>

- num1 and num2 are valid complex numbers.

<h2>Solution</h2>

```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1,i1 = num1.split("+")
        r2,i2 = num2.split("+")
        r1,i1 = int(r1),int(i1[:i1.index('i')])
        r2,i2 = int(r2),int(i2[:i2.index('i')])
        # print(r1,i1)
        # print(r2,i2)
        nr = (r1*r2) - (i1*i2) 
        ni = (r1*i2+r2*i1)
        # print(nr,ni)
        return "{0}+{1}i".format(str(nr),str(ni))
```
