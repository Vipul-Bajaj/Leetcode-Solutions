# [Home](./../..)/[Amazon](./..)/[Hard](./)/Orderly_Queue
<h1>Orderly Queue</h1>

<p>
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..
</p>
<p>
Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
</p>

<b>Example 1:</b>

    Input: s = "cba", k = 1
    Output: "acb"
    Explanation: 
    In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
    In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

<b>Example 2:</b>

    Input: s = "baaca", k = 3
    Output: "aaabc"
    Explanation: 
    In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
<b>Constraints:</b>

- 1 <= k <= s.length <= 1000
- s consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:]+s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))
```
