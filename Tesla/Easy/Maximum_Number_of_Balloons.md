# [Home](./../..)/[Tesla](./..)/[Easy](./)/Maximum_Number_of_Balloons
<h1>Maximum Number of Balloons</h1>

<p>
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
</p>
<p>
You can use each character in text at most once. Return the maximum number of instances that can be formed.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG">

    Input: text = "nlaebolko"
    Output: 1

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG">

    Input: text = "loonbalxballpoon"
    Output: 2

<b>Example 3:</b>

    Input: text = "leetcode"
    Output: 0
<b>Constraints:</b>

- 1 <= text.length <= 104
- text consists of lower case English letters only.

<h2>Solution</h2>

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        n = 0
        while counter['b']>0 and counter['a']>0 and counter['l']>1 and counter['o']>1 and counter['n']>0:
            n+=1
            counter['b']-=1
            counter['a']-=1
            counter['l']-=2
            counter['o']-=2
            counter['n']-=1
        return n
```
