<h1>Decode String</h1>

<p>
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

<b>Example 1:</b>

    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    
<b>Example 2:</b>

    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    
<b>Example 3:</b>

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

<b>Constraints:</b>

- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'.
- s is guaranteed to be a valid input.
- All the integers in s are in the range [1, 300].

<h2>Solution</h2>

```python
class Solution:
    def decodeString(self, s: str) -> str:
        count_st = []
        string_st = []
        n = ""
        curr_s = ""
        for i in s:
            if i.isdigit():
                n+=i
            elif i.isalpha():
                curr_s+=i
            elif i == '[':
                count_st.append(n)
                string_st.append(curr_s)
                n = ""
                curr_s = ""
            else:
                n = int(count_st.pop())
                curr_s = n*curr_s
                curr_s = string_st.pop() + curr_s
                n = ""
        return curr_s
```
