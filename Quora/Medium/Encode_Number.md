# [Home](./../..)/[Quora](./..)/[Medium](./)/Encode_Number
<h1>Encode Number</h1>

<p>
Given a non-negative integer num, Return its encoding string.
</p>
<p>
The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:
<img src="https://assets.leetcode.com/uploads/2019/06/21/encode_number.png">
</p>

<b>Example 1:</b>

    Input: num = 23
    Output: "1000"

<b>Example 2:</b>

    Input: num = 107
    Output: "101100"

<b>Constraints:</b>

- 0 <= num <= 10^9

<h2>Solution</h2>

```python
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]
```
