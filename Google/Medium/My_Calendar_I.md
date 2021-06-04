# [Home](./../..)/[Google](./..)/[Medium](./)/My_Calendar_I
<h1>My Calendar I</h1>

<p>
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
</p>
<p>
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
</p>
<p>
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
</p>
<p>
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
</p>
<p>
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
</p>

<b>Example 1:</b>

    MyCalendar();
    MyCalendar.book(10, 20); // returns true
    MyCalendar.book(15, 25); // returns false
    MyCalendar.book(20, 30); // returns true
    Explanation: 
    The first event can be booked.  The second can't because time 15 is already booked by another event.
    The third event can be booked, as the first event takes every time less than 20, but not including 20.

<b>Constraints:</b>

- The number of calls to MyCalendar.book per test case will be at most 1000.
- In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

<h2>Solution</h2>

```python
class MyCalendar:

    def _append(self,index,interval):
        self.n+=1
        self.intervals.insert(index,interval)
        return True
    
    def __init__(self):
        self.intervals = []
        self.n = 0

    def book(self, start: int, end: int) -> bool:
        interval = (start,end)
        if not self.intervals:
            return self._append(0,interval)
        index = bisect_left(self.intervals,(start,end))
        if index == 0:
            if end<=self.intervals[0][0]:
                return self._append(index,interval)
        elif index == self.n:
            if start>=self.intervals[-1][1]:
                return self._append(index,interval)
        else:
            if start>=self.intervals[index-1][1] and end<=self.intervals[index][0]:
                return self._append(index,interval)
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```
