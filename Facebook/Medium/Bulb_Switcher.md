# [Home](./../..)/[Facebook](./..)/[Medium](./)/Bulb_Switcher
<h1>Bulb Switcher</h1>

<p>
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
</p>
<p>
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
</p>
<p>
Return the number of bulbs that are on after n rounds.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg">

    Input: n = 3
    Output: 1
    Explanation: At first, the three bulbs are [off, off, off].
    After the first round, the three bulbs are [on, on, on].
    After the second round, the three bulbs are [on, off, on].
    After the third round, the three bulbs are [on, off, off]. 
    So you should return 1 because there is only one bulb is on.
    
<b>Example 2:</b>

    Input: n = 0
    Output: 0

<b>Example 3:</b>

    Input: n = 1
    Output: 1

<b>Constraints:</b>

- 0 <= n <= 109

<h2>Solution</h2>

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))
```
