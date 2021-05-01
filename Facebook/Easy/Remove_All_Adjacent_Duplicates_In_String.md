<h1>Remove All Adjacent Duplicates In String</h1>

<p>
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

<b>Example 1:</b>

    Input: "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

<b>Constraints:</b>

- 1 <= S.length <= 20000
- S consists only of English lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def removeDuplicates(self, S: str) -> str:
        n = len(S)
        st = []
        
        for i in range(n):
            if st and st[-1] == S[i]:
                st.pop()
            else:
                st.append(S[i])
        
        return "".join(st)
```
