# [Home](./../..)/[Google](./..)/[Hard](./)/String_Transforms_Into_Another_String
<h1>String Transforms Into Another String</h1>

<p>
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.
</p>
<p>
In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
</p>
<p>
Return true if and only if you can transform str1 into str2.
</p>

<b>Example 1:</b>

    Input: str1 = "aabcc", str2 = "ccdee"
    Output: true
    Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

<b>Example 2:</b>

    Input: str1 = "leetcode", str2 = "codeleet"
    Output: false
    Explanation: There is no way to transform str1 to str2.
<b>Constraints:</b>

- 1 <= str1.length == str2.length <= 104
- str1 and str2 contain only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        mapping = {}
        for s1,s2 in zip(str1,str2):
            if mapping.setdefault(s1,s2)!=s2:
                return False
        
        return len(set(str2))<26
```
