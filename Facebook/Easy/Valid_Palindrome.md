# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Valid_Palindrome
# [Home](./../../..)/[Facebook](./../..)/[Easy](./..)/Valid_Palindrome
<h1>Valid Palindrome</h1>

<p>
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

</p>

<b>Example 1:</b>

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    
<b>Example 2:</b>

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

<b>Constraints:</b>

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

<h2>Solution</h2>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
                
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
        return True
```
