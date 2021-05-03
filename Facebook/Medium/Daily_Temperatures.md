# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Daily_Temperatures
<h1>Daily Temperatures</h1>

<p>
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

</p>

<b>Example 1:</b>

    Input: [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]

<b>Constraints:</b>

- The length of temperatures will be in the range [1, 30000]. 
- Each temperature will be an integer in the range [30, 100].

<h2>Solution</h2>

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        st = []
        ans = [0]*n
        
        for i in range(n-1,-1,-1):
            while st and T[i]>=T[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1]-i
            st.append(i)
        return ans
```
