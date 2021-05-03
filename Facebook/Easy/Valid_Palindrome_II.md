# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Valid_Palindrome_II
# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Valid_Palindrome_II
<h1>Valid Palindrome II</h1>

<p>
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

</p>

<b>Example 1:</b>

    Input: "aba"
    Output: True
    
<b>Example 2:</b>

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

<b>Constraints:</b>

- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

<h2>Solution</h2>

```python
class Solution:
    def is_palindrome(self,s,i,j):
        _s = s[i:j+1]
        if _s==_s[::-1]:
            return True
        return False
    
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i<j:
            if s[i].lower() != s[j].lower():
                if self.is_palindrome(s,i+1,j) or self.is_palindrome(s,i,j-1):
                    return True
                else:
                    return False
            
            i+=1
            j-=1
        return True
```
