# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Angle_Between_Hands_of_a_Clock
# [Home](./../../..)/[Microsoft](./../..)/[Medium](./..)/Angle_Between_Hands_of_a_Clock
<h1>Angle Between Hands of a Clock</h1>

<p>
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png">
  
    Input: hour = 12, minutes = 30
    Output: 165
    
<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png">

    Input: hour = 3, minutes = 30
    Output: 75
    
<b>Example 3:</b>

<img src="https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png">

    Input: hour = 3, minutes = 15
    Output: 7.5

<b>Constraints:</b>

- 1 <= hour <= 12
- 0 <= minutes <= 59
- Answers within 10^-5 of the actual value will be accepted as correct.

<h2>Solution</h2>

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        minutes_ang = minutes * 6
        hours_ang = (hour+minutes/60)*30
        ans = None
        if hours_ang > minutes_ang:
            ans = hours_ang-minutes_ang
        else:
            ans = minutes_ang-hours_ang
        return min(ans,360-ans)
```
