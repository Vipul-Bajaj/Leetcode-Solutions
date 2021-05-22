# [Home](./../..)/[Mercari](./..)/[Easy](./)/Crawler_Log_Folder
<h1>Crawler Log Folder</h1>

<p>
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:
</p>

* "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
* "./" : Remain in the same folder.
* "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

<p>
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
</p>
<p>
The file system starts in the main folder, then the operations in logs are performed.
</p>
<p>
Return the minimum number of operations needed to go back to the main folder after the change folder operations.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png">

    Input: logs = ["d1/","d2/","../","d21/","./"]
    Output: 2
    Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

<b>Example 2:</b>

<img src="https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png">

    Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
    Output: 3
    
<b>Example 3:</b>

    Input: logs = ["d1/","../","../","../"]
    Output: 0
    
<b>Constraints:</b>

- 1 <= logs.length <= 103
- 2 <= logs[i].length <= 10
- logs[i] contains lowercase English letters, digits, '.', and '/'.
- logs[i] follows the format described in the statement.
- Folder names consist of lowercase English letters and digits.

<h2>Solution</h2>

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for log in logs:
            log = log.split("/")
            if log[0] == ".":
                continue
            elif log[0] == '..':
                if st:
                    st.pop()
            else:
                st.append(log[0])
        return len(st)
```
