# [Home](./../..)/[Nutanix](./..)/[Medium](./)/Partitioning_Into_Minimum_Number_Of_Deci_Binary_Numbers
<h1>Partitioning Into Minimum Number Of Deci-Binary Numbers</h1>

<p>
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
</p>
<p>
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
</p>

<b>Example 1:</b>

    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32
    
<b>Example 2:</b>

    Input: n = "82734"
    Output: 8
    
<b>Example 3:</b>

    Input: n = "27346209830709182346"
    Output: 9

<b>Constraints:</b>

- 1 <= n.length <= 105
- n consists of only digits.
- n does not contain any leading zeros and represents a positive integer.

<h2>Solution</h2>

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
```
