# [Home](./../..)/[Google](./..)/[Hard](./)/Race_Car
<h1>Race Car</h1>

<p>
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
</p>

- When you get an instruction 'A', your car does the following:
  - position += speed
  - speed *= 2
- When you get an instruction 'R', your car does the following:
  - If your speed is positive then speed = -1
  - otherwise speed = 1
  
  Your position stays the same.

<p>
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.
</p>
<p>
Given a target position target, return the length of the shortest sequence of instructions to get there.
</p>

<b>Example 1:</b>

    Input: target = 3
    Output: 2
    Explanation: 
    The shortest instruction sequence is "AA".
    Your position goes from 0 --> 1 --> 3.

<b>Example 2:</b>

    Input: target = 6
    Output: 5
    Explanation: 
    The shortest instruction sequence is "AAARA".
    Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.


<b>Constraints:</b>

- 1 <= target <= 104

<h2>Solution</h2>

```python
class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(1,0)])
        visited = set([(1,0)])
        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                curr_speed, curr_pos = q.popleft()
                if curr_pos == target:
                    return dist
                # if A
                new_pos = curr_pos+curr_speed
                new_speed = curr_speed*2
                if (new_speed,new_pos) not in visited and abs(target-new_pos)<target:
                    visited.add((new_speed,new_pos))
                    q.append((new_speed,new_pos))
                new_pos = curr_pos
                new_speed = -1 if curr_speed>0 else 1
                if (new_speed,new_pos) not in visited and abs(target-new_pos)<target:
                    visited.add((new_speed,new_pos))
                    q.append((new_speed,new_pos))
            dist+=1
        
        return -1
```
