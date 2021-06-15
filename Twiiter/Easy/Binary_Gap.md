# [Home](./../..)/[Twiiter](./..)/[Easy](./)/Binary_Gap
<h1>Binary Gap</h1>

<p>
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
</p>
<p>
Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
</p>

<b>Example 1:</b>

    Input: n = 22
    Output: 2
    Explanation: 22 in binary is "10110".
    The first adjacent pair of 1's is "10110" with a distance of 2.
    The second adjacent pair of 1's is "10110" with a distance of 1.
    The answer is the largest of these two distances, which is 2.
    Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
    
<b>Example 2:</b>

    Input: n = 5
    Output: 2
    Explanation: 5 in binary is "101".
    
<b>Example 3:</b>

    Input: n = 6
    Output: 1
    Explanation: 6 in binary is "110".
    
<b>Example 4:</b>

    Input: n = 8
    Output: 0
    Explanation: 8 in binary is "1000".
    There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.

<b>Constraints:</b>

- 1 <= n <= 109

<h2>Solution</h2>

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        i = 0
        dist = 0
        while i<len(b) and b[i]!='1':
            i+=1
        j=i+1
        while j<len(b):
            if b[j]=='1':
                dist = max(abs(j-i),dist)
                i = j
            j+=1
            
        return dist
```
