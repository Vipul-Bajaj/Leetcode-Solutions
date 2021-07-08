# [Home](./../..)/[Uber](./..)/[Medium](./)/Merge_Strings_Alternately
<h1>Merge Strings Alternately</h1>

<p>
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
<br>
Return the merged string.
</p>

<b>Example 1:</b>
  
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
    
<b>Example 2:</b>
  
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s
    
<b>Example 3:</b>
    
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d

<b>Constraints:</b>

- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i,j = 0,0
        n1,n2 = len(word1),len(word2)
        while i<n1 and j<n2:
            merged.append(word1[i])
            merged.append(word2[j])
            i+=1
            j+=1
        while i<n1:
            merged.append(word1[i])
            i+=1
        while j<n2:
            merged.append(word2[j])
            j+=1
        return "".join(merged)
```
