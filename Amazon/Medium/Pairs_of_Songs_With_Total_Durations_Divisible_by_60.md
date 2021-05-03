# [Home](./../..)/[Amazon](./..)/[Medium](./)/Pairs_of_Songs_With_Total_Durations_Divisible_by_60
<h1>Pairs of Songs With Total Durations Divisible by 60</h1>

<p>
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

</p>

<b>Example 1:</b>

    Input: time = [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60
  
<b>Example 2:</b>

    Input: time = [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
<b>Constraints:</b>

    1 <= time.length <= 6 * 104
    1 <= time[i] <= 500


<h2>Solution</h2>

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        no_of_pairs = 0
        remainders = [0]*60 
        for t in time:
            if t % 60 ==0:
                no_of_pairs += remainders[0]
            else:
                no_of_pairs += remainders[60-t%60]
            remainders[t%60] +=1
        return no_of_pairs
```
