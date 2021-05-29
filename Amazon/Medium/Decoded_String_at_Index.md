# [Home](./../..)/[Amazon](./..)/[Medium](./)/Decoded_String_at_Index
<h1>Decoded String at Index</h1>

<p>
An encoded string s is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:
</p>

* If the character read is a letter, that letter is written onto the tape.
* If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.

<p>
Now for some encoded string s, and an index k, find and return the k-th letter (1 indexed) in the decoded string.
</p>

<b>Example 1:</b>

    Input: s = "leet2code3", k = 10
    Output: "o"
    Explanation: 
    The decoded string is "leetleetcodeleetleetcodeleetleetcode".
    The 10th letter in the string is "o".
    
<b>Example 2:</b>

    Input: s = "ha22", k = 5
    Output: "h"
    Explanation: 
    The decoded string is "hahahaha".  The 5th letter is "h".
    
<b>Example 3:</b>
    
    Input: s = "a2345678999999999999999", k = 1
    Output: "a"
    Explanation: 
    The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

<b>Constraints:</b>

- 2 <= s.length <= 100
- s will only contain lowercase letters and digits 2 through 9.
- s starts with a letter.
- 1 <= k <= 109
- It's guaranteed that k is less than or equal to the length of the decoded string.
- The decoded string is guaranteed to have less than 263 letters.

<h2>Solution</h2>

```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        # Find size = length of decoded string
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
```
