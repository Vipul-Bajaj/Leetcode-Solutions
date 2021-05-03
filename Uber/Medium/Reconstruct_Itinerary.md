# [Home](./../..)/[Uber](./..)/[Medium](./)/Reconstruct_Itinerary
<h1>Reconstruct Itinerary</h1>

<p>
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

</p>

<b>Example 1:</b>
  
 <img src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg"> 

    Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]
    
<b>Example 2:</b>
  
 <img src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg"> 

    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

<b>Constraints:</b>

- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi
<h2>Solution</h2>

```python
class Solution:
    def dfs(self,city,adj_list):
        if city in adj_list:
            destinations = adj_list[city]
            while destinations:
                next_dest = destinations.pop()
                self.dfs(next_dest,adj_list)
        self.ans.append(city)
        
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel = {}
        self.ans = []
        for arrival,dept in tickets:
            if arrival in travel:
                travel[arrival].append(dept)
            else:
                travel[arrival] = [dept]
        
        for origin, cities in travel.items():
            cities.sort(reverse=True)
        
        self.dfs("JFK",travel)
        
        return self.ans[::-1]
```
