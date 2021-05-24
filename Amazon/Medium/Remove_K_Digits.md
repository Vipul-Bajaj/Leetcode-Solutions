# [Home](./../..)/[Amazon](./..)/[Medium](./)/Remove_K_Digits
<h1>Remove K Digits</h1>

<p>
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
</p>

<b>Example 1:</b>

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    
<b>Example 2:</b>

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
    
<b>Example 3:</b>

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

<b>Constraints:</b>

- 1 <= k <= num.length <= 105
- num consists of only digits.
- num does not have any leading zeros except for the zero itself.

<h2>Solution</h2>

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return '0'
        count = k
        i = 0
        st  = []
        while i<n and count>0:
            if st and st[-1]>num[i]:
                st.pop()
                count-=1
            else:
                st.append(num[i])
                i+=1
        
        if count == 0:
            ans = "".join(st)+num[i:]
        else:
            ans = "".join(st[:n-k])
        ans = ans.lstrip('0')
        return ans if ans!='' else '0'
```
