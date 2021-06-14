# [Home](./../..)/[Lendingkart](./..)/[Medium](./)/Smallest_String_With_A_Given_Numeric_Value
<h1>Smallest String With A Given Numeric Value</h1>

<p>
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.
</p>
<p>
The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.
</p>
<p>
You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.
</p>
<p>
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
</p>

<b>Example 1:</b>

    Input: n = 3, k = 27
    Output: "aay"
    Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
    
<b>Example 2:</b>

    Input: n = 5, k = 73
    Output: "aaszz"

<b>Constraints:</b>

- 1 <= n <= 105
- n <= k <= 26 * n

<h2>Solution</h2>

```python
class Solution:
    # def recursive(self,)
    def getSmallestString(self, n: int, k: int) -> str:
        arr = ['']*n
        
        for i in range(n-1,-1,-1):
            ch = min(k-i,26)
            arr[i] = chr(ch+96)
            k-=ch
        return "".join(arr)
```
