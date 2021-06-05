# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Reverse_Words_in_a_String_II
<h1>Reverse Words in a String II</h1>

<p>
Given a character array s, reverse the order of the words.
</p>
<p>
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
</p>
<p>
Your code must solve the problem in-place, i.e. without allocating extra space.
</p>

<b>Example 1:</b>

    Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    
<b>Example 2:</b>

    Input: s = ["a"]
    Output: ["a"]

<b>Constraints:</b>

- 1 <= s.length <= 105
- s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
- There is at least one word in s.
- s does not contain leading or trailing spaces.
- All the words in s are guaranteed to be separated by a single space.
 
<h2>Solution</h2>

```python
class Solution:
    def reverse(self,l,start,end):
        while start<end:
            l[start],l[end] = l[end],l[start]
            start+=1
            end-=1
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        self.reverse(s,0,n-1)
        start = end = 0
        while start<n:
            while end<n and s[end]!=' ':
                end+=1
            self.reverse(s,start,end-1)
            start = end+1
            end = start
        # print(s)
```
