# [Home](./../..)/[Bloomberg](./..)/[Medium](./)/Remove_All_Adjacent_Duplicates_in_String_II
<h1>Remove All Adjacent Duplicates in String II</h1>

<p>
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

</p>

<b>Example 1:</b>

    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.
    
<b>Example 2:</b>

    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
    
<b>Example 3:</b>

    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

<b>Constraints:</b>

- 1 <= s.length <= 10^5
- 2 <= k <= 10^4
- s only contains lower case English letters.

<h2>Solution</h2>

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        n = len(s)
        for i in range(n):
            if st and st[-1][0] == s[i]:
                st[-1][1]+=1
            else:
                st.append([s[i],1])
            if st and st[-1][0] == s[i] and st[-1][1] == k:
                st.pop()
        s = ""
        while st:
            ele = st.pop()
            s = ele[0]*ele[1] + s
        
        return s
```
