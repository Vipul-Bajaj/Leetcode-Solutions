# [Home](./../..)/[Microsoft](./..)/[Easy](./)/Reverse_Only_Letters
<h1>Reverse Only Letters</h1>

<p>
Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
</p>

<b>Example 1:</b>

    Input: s = "ab-cd"
    Output: "dc-ba"
    
<b>Example 2:</b>

    Input: s = "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
    
<b>Example 3:</b>

    Input: s = "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"

<b>Constraints:</b>

- s.length <= 100
- 33 <= s[i].ASCIIcode <= 122 
- s doesn't contain \ or "

<h2>Solution</h2>

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i,j = 0,len(s)-1
        s = list(s)
        while i<j:
            if s[i].lower() not in 'abcdefghijklmnopqrstuvwxyz':
                i+=1
                continue
            if s[j].lower() not in 'abcdefghijklmnopqrstuvwxyz':
                j-=1
                continue
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        
        return "".join(s)
```
