# [Home](./../..)/[Apple](./..)/[Easy](./)/Reverse_String
<h1>Reverse String</h1>

<p>
Write a function that reverses a string. The input string is given as an array of characters s.

</p>

<b>Example 1:</b>

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    
<b>Example 2:</b>

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

<b>Constraints:</b>

- 1 <= s.length <= 105
- s[i] is a printable ascii character.

<h2>Solution</h2>

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0,len(s)-1
        
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
```
