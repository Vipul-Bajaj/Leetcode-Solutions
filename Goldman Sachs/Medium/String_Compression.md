# [Home](./../../..)/[Goldman Sachs](./../..)/[Medium](./..)/String_Compression
<h1>String Compression</h1>

<p>
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

</p>

<b>Example 1:</b>

    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
    
<b>Example 2:</b>

    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.
    
<b>Example 3:</b>

    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
    
<b>Example 4:</b>    

    Input: chars = ["a","a","a","b","b","a","a"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
    Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.

<b>Constraints:</b>

- 1 <= chars.length <= 2000
- chars[i] is a lower-case English letter, upper-case English letter, digit, or symbol.

<h2>Solution</h2>

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        current = 0
        j = 0
        n = len(chars)
        for i in range(n):
            if i+1 == n or chars[i+1]!=chars[i]:
                chars[j] = chars[current]
                j+=1
                if i > current:
                    for k in str(i-current+1):
                        chars[j] = k
                        j+=1
                current = i + 1
        return j
```
