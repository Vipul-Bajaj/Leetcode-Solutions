# [Home](./../..)/[Amazon](./..)/[Medium](./)/Count_Sorted_Vowel_Strings
<h1>Count Sorted Vowel Strings</h1>

<p>
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
</p>
<p>
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
</p>

<b>Example 1:</b>

    Input: n = 1
    Output: 5
    Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
    
<b>Example 2:</b>

    Input: n = 2
    Output: 15
    Explanation: The 15 sorted strings that consist of vowels only are
    ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
    Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
    
<b>Example 3:</b>

    Input: n = 33
    Output: 66045

<b>Constraints:</b>

- 1 <= n <= 50 

<h2>Solution</h2>

```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # arr = [1]*5
        # for i in range(1,n):
        #     for j in range(5):
        #         arr[j] = sum(arr[j:])
        # return sum(arr)
        return (n+4)*(n+3)*(n+2)*(n+1)//24
```
