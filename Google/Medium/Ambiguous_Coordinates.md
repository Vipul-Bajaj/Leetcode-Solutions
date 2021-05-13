# [Home](./../..)/[Google](./..)/[Medium](./)/Ambiguous_Coordinates
<h1>Ambiguous Coordinates</h1>

<p>
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)
</p>

<b>Example 1:</b>

    Input: s = "(123)"
    Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
  
<b>Example 2:</b>

    Input: s = "(00011)"
    Output:  ["(0.001, 1)", "(0, 0.011)"]
    Explanation: 
    0.0, 00, 0001 or 00.01 are not allowed.

<b>Example 3:</b>

    Input: s = "(0123)"
    Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    
<b>Example 4:</b>

    Input: s = "(100)"
    Output: [(10, 0)]
    Explanation: 
    1.0 is not allowed.
 
<b>Constraints:</b>

* 4 <= s.length <= 12.
* s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.

<h2>Solution</h2>

```python
def hasLeadingZeros(s):
    n = len(s)
    if n>=2:
        if s[0] == '0' and s[1].isdigit():
            return True
        dot_ind = s.find('.')
        if dot_ind !=-1:
            if (s[dot_ind-1] == '0' and s[dot_ind+1] == '0' and s[-1] == '0') or s[-1]=='0':
                return True
    return False
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s_coordinates = s[1:-1]
        comma_cordinates = set()
        n = len(s_coordinates)
        for i in range(1,n):
            first = s_coordinates[:i]
            second = s_coordinates[i:]
            comma_cordinates.add((first,second))
        # print(comma_cordinates)
        decimal_cordinates = set()
        for comma_cordinate in comma_cordinates:
            first,second = comma_cordinate
            for j in range(1,len(second)):
                sdec = second[:j]+"."+second[j:]
                decimal_cordinates.add((first,sdec))
            for i in range(1,len(first)):
                fdec = first[:i]+"."+first[i:]
                decimal_cordinates.add((fdec,second))
            for i in range(1,len(first)):
                fdec = first[:i]+"."+first[i:]
                decimal_cordinates.add((fdec,second))
                for j in range(1,len(second)):
                    sdec = second[:j]+"."+second[j:]
                    decimal_cordinates.add((fdec,sdec))
                    decimal_cordinates.add((first,sdec))
        # print(decimal_cordinates)
        out = []
        for cordinates in comma_cordinates.union(decimal_cordinates):
            first,second = cordinates
            if not hasLeadingZeros(first) and not hasLeadingZeros(second):
                out.append("({}, {})".format(first,second))
        return out
```
