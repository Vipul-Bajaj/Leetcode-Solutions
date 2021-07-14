# [Home](./../..)/[Facebook](./..)/[Medium](./)/Custom_Sort_String
<h1>Custom Sort String</h1>

<p>
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.
</p>
<p>
order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.
</p>
<p>
Return any permutation of str (as a string) that satisfies this property.
</p>

<b>Example 1:</b>

    Input: 
    order = "cba"
    str = "abcd"
    Output: "cbad"
    Explanation: 
    "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
    Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

<b>Constraints:</b>

- order has length at most 26, and no character is repeated in order.
- str has length at most 200.
- order and str consist of lowercase letters only.

<h2>Solution</h2>

```python
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count = Counter(str)
        out = []
        for ch in order:
            if ch in count:
                out.extend([ch]*count[ch])
                del count[ch]
        for ch in count.keys():
            out.extend([ch]*count[ch])
        return "".join(out)
```
