# [Home](./../..)/[Google](./..)/[Easy](./)/Employee_Importance
<h1>Employee Importance</h1>

<p>
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

</p>

<b>Example 1:</b>

    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11
    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

<b>Note:</b>
1. One employee has at most one direct leader and may have several subordinates.
2. The maximum number of employees won't exceed 2000.


<h2>Solution</h2>

```python
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates = {}
        importance = {}
        
        for employee in employees:
            importance[employee.id] = employee.importance
            if employee.id not in subordinates:
                subordinates[employee.id] = employee.subordinates
        
        q = [id]
        ans = 0
        while q:
            ele = q.pop(0)
            ans += importance[ele]
            q += subordinates[ele]
            
        return ans
```
