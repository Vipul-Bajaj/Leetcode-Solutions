# [Home](./../..)/[Google](./..)/[Easy](./)/Student_Attendance_Record_I
<h1>Student Attendance Record I</h1>

<p>
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
</p>

* 'A': Absent.
* 'L': Late.
* 'P': Present.

<p>
The student is eligible for an attendance award if they meet both of the following criteria:
</p>

* The student was absent ('A') for strictly fewer than 2 days total.
* The student was never late ('L') for 3 or more consecutive days.

<p>
Return true if the student is eligible for an attendance award, or false otherwise.
</p>

<b>Example 1:</b>

    Input: s = "PPALLP"
    Output: true
    Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

<b>Example 2:</b>

    Input: s = "PPALLL"
    Output: false
    Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.


<b>Constraint:</b>
- 1 <= s.length <= 1000
- s[i] is either 'A', 'L', or 'P'.

<h2>Solution</h2>

```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A')<=1 and not 'LLL' in s
```
