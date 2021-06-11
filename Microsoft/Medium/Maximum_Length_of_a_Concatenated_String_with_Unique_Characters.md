# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Maximum_Length_of_a_Concatenated_String_with_Unique_Characters
<h1>Maximum Length of a Concatenated String with Unique Characters</h1>

<p>
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
</p>
<p>
Return the maximum possible length of s.
</p>

<b>Example 1:</b>

    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
    Maximum length is 4.
    
<b>Example 2:</b>

    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible solutions are "chaers" and "acters".
      
<b>Example 3:</b>

    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    
<b>Constraints:</b>

- 1 <= arr.length <= 16
- 1 <= arr[i].length <= 26
- arr[i] contains only lower case English letters.

<h2>Solution</h2>

```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = ['']
        
        def isvalid(s):
            return len(s) == len(set(s))
        
        for word in arr:
            for j in unique:
                tmp = word + j
                if isvalid(tmp):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen
```
