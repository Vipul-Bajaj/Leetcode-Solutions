# [Home](./../..)/[Facebook](./..)/[Easy](./)/Reverse_Vowels_of_a_String
<h1>Reverse Vowels of a String</h1>

<p>
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
</p>

<b>Example 1:</b>

    Input: s = "hello"
    Output: "holle"
    
<b>Example 2:</b>

    Input: s = "leetcode"
    Output: "leotcede"

<b>Constraints:</b>

- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

<h2>Solution</h2>

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l,r = 0,n-1
        vowels = 'AEIOUaeiou'
        while l<r:
            while l<n and s[l] not in vowels:
                l+=1
            while r>=0 and s[r] not in vowels:
                r-=1
            if l<r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
```
