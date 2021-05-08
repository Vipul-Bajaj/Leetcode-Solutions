# [Home](./../..)/[Infosys](./..)/[Medium](./)/Maximum_Number_of_Events_That_Can_Be_Attended
<h1>Maximum Number of Events That Can Be Attended</h1>

<p>
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
</p>

<b>Example 1:</b>

    Input: events = [[1,2],[2,3],[3,4]]
    Output: 3
    Explanation: You can attend all the three events.
    One way to attend them all is as shown.
    Attend the first event on day 1.
    Attend the second event on day 2.
    Attend the third event on day 3.

<b>Example 2:</b>

    Input: events= [[1,2],[2,3],[3,4],[1,2]]
    Output: 4
    
<b>Example 3:</b>
    
    Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    Output: 4
    
<b>Example 4:</b>
    
    Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    Output: 7

<b>Constraints:</b>

- 1 <= events.length <= 105
- events[i].length == 2
- 1 <= startDayi <= endDayi <= 105

<h2>Solution</h2>

```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        c = 0
        start = min(s for s,e in events)
        end = max(e for s,e in events)
        i = 0
        h = []
        for day in range(start,end+1):
            while i<n and events[i][0]==day:
                heapq.heappush(h,events[i][1])
                i+=1
            while h and h[0] < day:
                heapq.heappop(h)

            # event to attend today is the one at the top of the heap
            if h:
                heapq.heappop(h)
                c += 1
        return c
```
