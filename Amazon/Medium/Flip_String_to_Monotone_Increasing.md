# [Home](./../..)/[Amazon](./..)/[Medium](./)/Flip_String_to_Monotone_Increasing
<h1>Flip String to Monotone Increasing</h1>

<p>
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
</p>
<p>
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
</p>
<p>
Return the minimum number of flips to make s monotone increasing.
</p>

<b>Example 1:</b>

    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.

<b>Example 2:</b>

    Input: s = "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.

<b>Example 3:</b>

    Input: s = "00011000"
    Output: 2
    Explanation: We flip to get 00000000.

<b>Constraints:</b>

- 1 <= s.length <= 105
- s[i] is either '0' or '1'.

<h2>Solution</h2>

```python
class Solution(object):
    def minFlipsMonoIncr(self, S):
#         P = [0]
#         for x in S:
#             P.append(P[-1] + int(x))

#         return min(P[j] + len(S)-j-(P[-1]-P[j])
#                    for j in range(len(P)))
        dp=0
        c=0
        for i in S:
            if i=='1':
                c+=1
            else:
                dp=min(dp+1,c)
        return dp
```
