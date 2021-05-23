# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Kill_Process
<h1>Kill Process</h1>

<p>
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
</p>
<p>
Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).
</p>
<p>
When a process is killed, all of its children processes will also be killed.
</p>
<p>
Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/02/24/ptree.jpg">

    Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
    Output: [5,10]
    Explanation: The processes colored in red are the processes that should be killed.
    
<b>Example 2:</b>

    Input: pid = [1], ppid = [0], kill = 1
    Output: [1]

<b>Constraints:</b>

- n == pid.length
- n == ppid.length
- 1 <= n <= 5 * 104
- 1 <= pid[i] <= 5 * 104
- 0 <= ppid[i] <= 5 * 104
- Only one process has no parent.
- All the values of pid are unique.
- kill is guaranteed to be in pid.

<h2>Solution</h2>

```python
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_child = defaultdict(list)
        for i in range(len(ppid)):
            if ppid[i] == 0:
                continue
            parent_child[ppid[i]].append(pid[i])
        
        q = deque([kill])
        killed = set([kill])
        
        while q:
            killing = q.popleft()
            for process in parent_child[killing]:
                if process not in killed:
                    killed.add(process)
                    q.append(process)
        return killed
```
